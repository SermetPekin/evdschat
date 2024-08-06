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


from evdschat import chat
import pandas as pd


def test_chat(capsys):

    prompt = """

    Can I get reserves data please ? Aylık frekans istiyorum. ortalama olarak toplulaştırır mısın? 
    
    
    """
    with capsys.disabled():
        res, notes = chat(prompt, debug=False, force=False )
        print(res)
        assert isinstance(res.data, pd.DataFrame)
