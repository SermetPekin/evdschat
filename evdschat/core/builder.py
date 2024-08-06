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

import traceback
from dataclasses import dataclass, field

from ..model.chatters import ModelAbstract, OpenAI
from ..common.akeys import ApiKey, OpenaiApiKey, get_openai_key


@dataclass
class Builder:
    retriever = field(default_factory=ModelAbstract)
    api_key = field(default_factory=ApiKey)


def build_openai():

    builder = Builder(OpenAI(), OpenaiApiKey(get_openai_key()))
    return builder
