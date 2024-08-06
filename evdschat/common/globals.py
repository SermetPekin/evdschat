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


def global_mock():
    template = """ 
TP_GSYIH01_GY_CF #
TP_GSYIH02_GY_CF #
TP_GSYIH03_GY_CF
TP_GSYIH04_GY_CF 
TP_GSYIH05_GY_CF
TP_GSYIH06_GY_CF
TP_GSYIH07_GY_CF
TP_GSYIH08_GY_CF

        """
    return {
        "index": template,
        "start_date": "31-12-2009",
        "frequency": "monthly",
        "aggregation": "end",
        "notes": "Note: This is a mock result for testing purposes... in order to get real results call the same function with test=False ",
    }
