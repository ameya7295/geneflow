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

from .load_backend import backend  # noqa: F401

# -initialization-
from .load_backend import copy  # noqa: F401
from .load_backend import zeros  # noqa: F401
from .load_backend import ones  # noqa: F401
from .load_backend import full  # noqa: F401
from .load_backend import normal  # noqa: F401

# - reduce -
from .load_backend import prod  # noqa: F401
from .load_backend import max  # noqa: F401
from .load_backend import min  # noqa: F401
from .load_backend import sum  # noqa: F401
from .load_backend import mean  # noqa: F401

# - Manipulation -
from .load_backend import tile  # noqa: F401
from .load_backend import tensor  # noqa: F401
from .load_backend import concatenate  # noqa: F401

# - Utils -
from .load_backend import flatten  # noqa: F401
from .load_backend import as_numpy_array  # noqa: F401
from .load_backend import reshape  # noqa: F401
from .load_backend import is_tensor  # noqa: F401
from .load_backend import tensor_equal  # noqa: F401
from .load_backend import allclose  # noqa: F401

# - Math -
from .load_backend import dot  # noqa: F401
from .load_backend import add  # noqa: F401
from .load_backend import subtract  # noqa: F401
from .load_backend import multiply  # noqa: F401
from .load_backend import divide  # noqa: F401
from .load_backend import mod  # noqa: F401
from .load_backend import clip  # noqa: F401
from .load_backend import abs  # noqa: F401
from .load_backend import absolute  # noqa: F401
from .load_backend import norm  # noqa: F401

# - Randomness -
from .load_backend import randint  # noqa: F401
from .load_backend import shuffle  # noqa: F401
from .load_backend import full_shuffle  # noqa: F401

# - Indexing -
from .load_backend import take  # noqa: F401
from .load_backend import bottom_k_indices  # noqa: F401
from .load_backend import top_k_indices  # noqa: F401

# - Statistical -
from .load_backend import bincount  # noqa: F401
