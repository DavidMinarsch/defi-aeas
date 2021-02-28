# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021 defi-aeas
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the tokens the agent has interacted with."""

# pylint: disable=import-error,no-name-in-module
from packages.defi_aeas.skills.capital_allocation.abstract import (
    OnChainItem,
    OnChainItemCollection,
)


# pylint: enable=import-error,no-name-in-module

TokenAddress = str


class Token(OnChainItem):
    """The token is a represenation of an on-chain token (ERC-20)."""

    onchain_id: TokenAddress
    name: str
    symbol: str


class Tokens(OnChainItemCollection):
    """The tokens class keeps track of all tokens interacted with by the agent."""

    item_class = Token
