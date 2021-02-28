# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2020 Fetch.AI Limited
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

"""This module contains the uniswap_v2_router_02 contract definition."""

import logging

from aea.common import JSONLike
from aea.configurations.base import PublicId
from aea.contracts.base import Contract
from aea.crypto.base import LedgerApi


_default_logger = logging.getLogger(
    "aea.packages.defi_aeas.contracts.erc20.contract"
)

PUBLIC_ID = PublicId.from_str("defi_aeas/erc20:0.1.0")


class ERC20Contract(Contract):
    """The ERC20 contract class which acts as a bridge between AEA framework and ERC20 ABI."""

    contract_id = PUBLIC_ID


    @classmethod
    def get_raw_transaction(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> Optional[JSONLike]:
        """
        Handler method for the 'GET_RAW_TRANSACTION' requests.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :return: the tx
        """
        raise NotImplementedError
