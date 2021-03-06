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

from .op import OP
import geneflow.backend as B


class Input(OP):
    def __init__(self, shape, **kwargs):
        """Input op

        Args:
            shape (set of ints): what is the shape of the input to the
            evolutionary graph. Its of the form
            (num_chromosme, chromosome_dim_1, .... chromesome_dim_n)

            name (str, optional): Name of the OP. Should be unique in a graph
            (do not reuse the same name twice). It will be autogenerated
            if it isn't provided.
        """
        self.shape = shape
        super(Input, self).__init__(**kwargs)

    def get_output_shapes(self):
        "return the shape of tensor returned by the op"
        return self.shape

    def assign(self, chromosomes):
        """Assign concrete values to the input
        """
        chromosomes = B.tensor(chromosomes)

        if chromosomes.shape != self.shape:
            raise ValueError(
                'Incompatible input shape expected: %s - got: %s' %
                (self.shape, chromosomes.shape))
        self.chromosomes = chromosomes

    def call(self, unused):
        "make it compatible with other ops"
        return self.chromosomes

    def get(self):
        "shorthand version which is used inside our main loop"
        return self.chromosomes