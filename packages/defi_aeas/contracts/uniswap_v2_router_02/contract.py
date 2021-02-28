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

from aea.common import Address, JSONLike
from aea.configurations.base import PublicId
from aea.contracts.base import Contract
from aea.crypto.base import LedgerApi
from aea.crypto.ethereum import EthereumApi


_default_logger = logging.getLogger(
    "aea.packages.defi_aeas.contracts.uniswap_v2_router_02.contract"
)

PUBLIC_ID = PublicId.from_str("defi_aeas/uniswap_v2_router_02:0.1.0")


class UniswapV2Router02Contract(Contract):
    """The UniswapV2Router contract class which acts as a bridge between AEA framework and UniswapV2Router ABI."""

    contract_id = PUBLIC_ID

    @classmethod
    def get_add_liquidity(
        cls,
        ledger_api: LedgerApi,
        sender_address: Address,
        contract_address: Address,
        token_a: Address,
        token_b: Address,
        amount_a_desired: int,
        amount_b_desired: int,
        amount_a_min: int,
        amount_b_min: int,
        to: Address,
        deadline: int,
        gas: int,
        gas_price: int,
    ) -> JSONLike:
        """
        Get the add_liquidity transaction.

        For details see https://uniswap.org/docs/v2/smart-contracts/router02/#addliquidity.

        :param ledger_api: the ledger api
        :param sender_address: the address of the sender of the tx.
        :param contract_address: the address of the deployed contract.
        :param token_a: The contract address of the desired token.
        :param token_b: The contract address of the desired token.
        :param amount_a_desired: The amount of tokenA to add as liquidity if the B/A price is <= amountBDesired/amountADesired (A depreciates).
        :param amount_b_desired: The amount of tokenB to add as liquidity if the A/B price is <= amountADesired/amountBDesired (B depreciates).
        :param amount_a_min: Bounds the extent to which the B/A price can go up before the transaction reverts. Must be <= amountADesired.
        :param amount_b_min: Bounds the extent to which the A/B price can go up before the transaction reverts. Must be <= amountBDesired.
        :param to: Recipient of the liquidity tokens.
        :param deadline: Unix timestamp after which the transaction will revert.
        :return: the transaction object
        """
        if ledger_api.identifier != EthereumApi.identifier:
            raise ValueError(f"Only {EthereumApi.identifier} is supported!")
        nonce = ledger_api.api.eth.getTransactionCount(sender_address)
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.addLiquidity(
            token_a,
            token_b,
            amount_a_desired,
            amount_b_desired,
            amount_a_min,
            amount_b_min,
            to,
            deadline,
        ).buildTransaction({"gas": gas, "gasPrice": gas_price, "nonce": nonce})
        return tx

    @classmethod
    def get_add_liquidity_eth(
        cls,
        ledger_api: LedgerApi,
        sender_address: Address,
        contract_address: Address,
        token: Address,
        amount_token_desired: int,
        amount_eth_desired: int,
        amount_token_min: int,
        amount_eth_min: int,
        to: Address,
        deadline: int,
        gas: int,
        gas_price: int,
    ) -> JSONLike:
        """
        Get the add_liquidity transaction.

        For details see https://uniswap.org/docs/v2/smart-contracts/router02/#addliquidityeth.

        :param ledger_api: the ledger api
        :param sender_address: the address of the sender of the tx.
        :param contract_address: the address of the deployed contract.
        :param token: The contract address of the desired token.
        :param amount_token_desired: The amount of token to add as liquidity if the WETH/token price is <= msg.value/amountTokenDesired (token depreciates).
        :param amount_eth_desired: The amount of ETH to add as liquidity if the token/WETH price is <= amountTokenDesired/msg.value (WETH depreciates).
        :param amount_token_min: Bounds the extent to which the WETH/token price can go up before the transaction reverts. Must be <= amountTokenDesired.
        :param amount_eth_min: Bounds the extent to which the token/WETH price can go up before the transaction reverts. Must be <= msg.value.
        :param to: Recipient of the liquidity tokens.
        :param deadline: Unix timestamp after which the transaction will revert.
        :return: the transaction object
        """
        if ledger_api.identifier != EthereumApi.identifier:
            raise ValueError(f"Only {EthereumApi.identifier} is supported!")
        nonce = ledger_api.api.eth.getTransactionCount(sender_address)
        instance = cls.get_instance(ledger_api, contract_address)
        tx = instance.functions.addLiquidityEth(
            token, amount_token_desired, amount_token_min, amount_eth_min, to, deadline
        ).buildTransaction(
            {
                "from": sender_address,
                "value": amount_eth_desired,
                "gas": gas,
                "gasPrice": gas_price,
                "nonce": nonce,
            }
        )
        return tx
