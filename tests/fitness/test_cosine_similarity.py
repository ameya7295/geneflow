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

from geneflow.fitness import InvertedCosineSimilarity
import geneflow.backend as B


def test_cosine_similarity_1dpopulation(backends):
    "test the function works on a population and broadcast correctly"

    reference = [1, 0, 1, 1, 0, 1, 1, 1]
    different = [1, 1, 1, 0, 1, 1, 1, 1]

    r = B.tensor(reference)
    d = B.tensor(different)
    population = B.tensor([r, d, r])
    cs = InvertedCosineSimilarity(r)

    # similar vector have a distance of 1
    distances = cs(population)
    print("distances", distances)
    assert int(distances[0]) == 1
    assert distances[1] < 1
    assert int(distances[2]) == 1


def test_cosine_2d(backends):
    INSERTION_POINTS = [0, 10, 20]  # where we copy the ref chromosome

    ref_chromosome = B.randint(0, 2, (32, 32))
    ref_pop = B.randint(0, 2, (64, 32, 32))

    for idx in INSERTION_POINTS:
        ref_pop[idx] = ref_chromosome

    cs = InvertedCosineSimilarity(ref_chromosome)
    distances = cs(ref_pop)

    for idx, dst in enumerate(distances):
        if idx in INSERTION_POINTS:
            assert int(dst) == 1
        else:
            assert dst < 1
            assert dst > 0
