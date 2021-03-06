# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from geneflow.engine import OP
from geneflow import backend as B


class SingleCrossover(OP):
    def __init__(self, population_fraction, crossover_probability, **kwargs):
        """Perform single crossovers on a given population.

        Args:
            population_fraction (float): How many chromosomes
            should have a cross-over.

            crossover_probability (list(float)): What fraction of the
            gene should be affected by crossovers.

            debug (bool, optional): print debug information and function
            returns additional data.

        Returns:
            tensor: population with a crossover

        See:
            https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)
        """

        if not (0 < population_fraction <= 1.0):
            raise ValueError("num_crossover_fraction must be in ]0. 1]")

        for val in crossover_probability:
            if not (0 < val <= 1.0):
                raise ValueError(
                    "crossover_probability values must be between ]0. 1]")

        self.population_fraction = population_fraction
        self.crossover_probability = crossover_probability
        self.has_cache = False
        self.mutation_shape = []
        self.slices = None
        super(SingleCrossover, self).__init__(**kwargs)

    def call(self, populations):
        results = []
        for population in populations:
            results.append(self.compute(population))
        return results

    def compute(self, population):

        # mix genomes
        population_copy = B.copy(population)
        B.shuffle(population_copy)

        # how many chromosomes to crossover
        num_crossovers = int(population.shape[0] * self.population_fraction)

        if self.debug:
            print('num_crossovers', num_crossovers)

        if not self.has_cache:
            self.print_debug("Caching fancy indexing")
            self.has_cache = True

            # compute the shape needed for the mutation
            mutations_shape = [num_crossovers]
            for idx, frac in enumerate(self.crossover_probability):
                num_genes = int(population.shape[idx + 1] * frac)
                mutations_shape.append(num_genes)
            self.print_debug("mutation_shape: %s" % mutations_shape)

            # compute the fancy indexing dynamlically
            # note: Contrary to dual_crossover, for single crossover we don't
            # need to randomizes the starting point.
            slices = []
            for crossover_size in mutations_shape:
                slices.append(slice(0, crossover_size))
            self.slices = tuple(slices)

        else:
            self.print_debug("Using cached fancy indexing")

        # crossover
        cross_section = population_copy[self.slices]
        population[self.slices] = cross_section

        return population


class SingleCrossover1D(SingleCrossover):
    def __init__(self,
                 population_fraction=0.9,
                 crossover_probability=0.2,
                 **kwargs):
        if not isinstance(crossover_probability, float):
            raise ValueError('crossover_probability must be a float')

        super(SingleCrossover1D,
              self).__init__(population_fraction=population_fraction,
                             crossover_probability=[crossover_probability],
                             **kwargs)


class SingleCrossover2D(SingleCrossover):
    def __init__(self,
                 population_fraction=0.9,
                 crossover_probability=(0.2, 0.2),
                 **kwargs):

        if len(crossover_probability) != 2:
            raise ValueError('crossover_probability must be of form (x, y)')
        super(SingleCrossover2D,
              self).__init__(population_fraction=population_fraction,
                             crossover_probability=crossover_probability,
                             **kwargs)


class SingleCrossover3D(SingleCrossover):
    def __init__(self,
                 population_fraction=0.9,
                 crossover_probability=(0.2, 0.2, 0.2),
                 **kwargs):

        if len(crossover_probability) != 3:
            raise ValueError('crossover_probability must be of form (x, y, z)')

        super(SingleCrossover3D,
              self).__init__(population_fraction=population_fraction,
                             crossover_probability=crossover_probability,
                             **kwargs)


if __name__ == '__main__':
    from copy import copy
    print(B.backend())
    GENOME_SHAPE = (6, 4, 4)
    population = B.randint(0, 256, GENOME_SHAPE)
    population_fraction = 0.5
    max_crossover_size_fraction = (0.5, 0.5)
    print(population.shape)
    original_population = copy(population)
    population = SingleCrossover2D(population_fraction,
                                   max_crossover_size_fraction,
                                   debug=True)(population)

    # diff matrix
    diff = B.clip(abs(population - original_population), 0, 1)
    print(diff)
