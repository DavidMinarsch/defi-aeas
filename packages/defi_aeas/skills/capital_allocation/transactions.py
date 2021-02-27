# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright defi-aeas
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

"""This module contains the transactions the agent has completed."""

from datetime import datetime

# pylint: disable=import-error,no-name-in-module
from packages.defi_aeas.skills.capital_allocation.abstract import (
    OnChainItem,
    OnChainItemCollection,
)


# pylint: enable=import-error,no-name-in-module

TransactionHash = str


class Transaction(OnChainItem):
    """The transaction is a representation of an on-chain transaction."""

    onchain_id: TransactionHash
    amount: int
    denomination: str
    currency: int
    timestamp: datetime
    from_address: str
    to_address: str


class Transactions(OnChainItemCollection):
    """The transactions class keeps track of all transactions completed by the agent."""

    item_class = Transaction
