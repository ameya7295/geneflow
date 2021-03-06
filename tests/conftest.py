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

import pytest
import logging


@pytest.fixture(scope="session")
def backends():
    """constructing a list of backend

    # ! only use this for backend testing. Higher level function import the
    # ! backend so it will create type conflict.
    """
    import geneflow.backend.numpy as NP
    logger = logging.getLogger()

    try:
        import cupy  # noqa
        logger.info('cupy found')
    except:  # noqa
        import geneflow.backend.numpy as CP
        logger.info('cupy not found - using numpy instead')
    else:
        import geneflow.backend.cupy as CP

    return [NP, CP]
