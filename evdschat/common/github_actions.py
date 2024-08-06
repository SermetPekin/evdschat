# evdschat - An open-source Python package for enhanced data retrieval.
# Copyright (c) 2024 Sermet Pekin
# Licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://creativecommons.org/licenses/by-nc/4.0/
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
class GithubActions:
    def is_testing(self):
        return "hostedtoolcache" in sys.argv[0]
class PytestTesting:
    def is_testing(self):
        # print(" sys.argv[0]" ,  sys.argv[0])
        return "pytest" in sys.argv[0]
def get_input(msg, default=None):
    if GithubActions().is_testing() or PytestTesting().is_testing():
        if not default:
            print("currently testing with no default ")
            return False
        return default
    return  input(msg)