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

"""This module contains the pools the agent has interacted with."""

from enum import Enum
from typing import Tuple

# pylint: disable=import-error,no-name-in-module
from packages.defi_aeas.skills.capital_allocation.abstract import (
    OnChainItem,
    OnChainItemCollection,
)
from packages.defi_aeas.skills.capital_allocation.tokens import Token


# pylint: enable=import-error,no-name-in-module

PoolAddress = str


class PoolStatus(Enum):
    """The status of a pool as viewed by the agent."""

    NO_PROVISION = "no_provision"
    PROVISION_PENDING = "provision_pending"
    PROVISION_ACTIVE = "provision_active"
    WITHDRAWAL_PENDING = "withdrawal_pending"
    WITHDRAWAL_COMPLETE = "withdrawal_complete"


class Pool(OnChainItem):
    """The token is a represenation of an on-chain token (ERC-20)."""

    onchain_id: PoolAddress
    pair: Tuple[Token, Token]


class Pools(OnChainItemCollection):
    """The pools class keeps track of all pools interacted with by the agent."""

    item_class = Pool
