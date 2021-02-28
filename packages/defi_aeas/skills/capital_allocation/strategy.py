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

"""This module contains the ABC used throughout the skill."""

from enum import Enum
from typing import Dict, List, Optional, cast

from aea.skills.base import Model

# pylint: disable=import-error,no-name-in-module
from packages.defi_aeas.skills.capital_allocation.pools import (
    Pool,
    PoolAddress,
    PoolStatus,
)
from packages.defi_aeas.skills.capital_allocation.tokens import TokenAddress, Tokens


# pylint: enable=import-error,no-name-in-module


class AgentStatus(Enum):
    """Agent status."""

    ACTIVE = "active"
    PAUSED = "paused"


class Strategy(Model):
    """Strategy parameters and management."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize dialogues.

        :return: None
        """
        Model.__init__(self, **kwargs)
        self._token_whitelist: List[PoolAddress] = []
        self._pool_statuses: Dict[Pool, PoolStatus]
        self._active_pool: Optional[Pool] = None
        self._next_active_pool: Optional[Pool] = None
        self._agent_status: AgentStatus = AgentStatus.PAUSED

    @property
    def token_whitelist(self) -> List[PoolAddress]:
        """Get the token whitelist."""
        return self._token_whitelist

    @property
    def agent_status(self) -> AgentStatus:
        """Get agent status."""
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status: AgentStatus) -> None:
        """Set the agent status."""
        self._agent_status = agent_status

    @property
    def active_pool(self) -> Optional[Pool]:
        """Get active pool."""
        return self._active_pool

    @active_pool.setter
    def active_pool(self, active_pool: Optional[Pool]) -> None:
        """Set the active pool."""
        self._active_pool = active_pool

    def update_pool_status(self, pool: Pool, new_status: PoolStatus) -> None:
        """Update the pool status of the pool."""
        self._pool_statuses[pool] = new_status

    def add_to_whitelist(self, token_addresses: List[TokenAddress]) -> None:
        """Add a list of tokens to the whitelist."""
        for token_address in token_addresses:
            if cast(Tokens, self.context.tokens).get(token_address) is None:
                # probably fetch token info and then add?
                continue
            if token_address in self._token_whitelist:
                continue
            self._token_whitelist.append(token_address)

    def remove_from_whitelist(self, token_addresses: List[TokenAddress]) -> None:
        """Remove a list of tokens from the whitelist."""
        for token_address in token_addresses:
            if token_address not in self._token_whitelist:
                continue
            self._token_whitelist.remove(token_address)

    def get_pool_with_highest_apr_forecast(self) -> Optional[Pool]:
        """Get the pool with the highest APR forecast."""
        raise NotImplementedError

    def is_rebalancing_profitable(
        self, current_pool: Optional[Pool], next_pool: Optional[Pool]
    ) -> bool:
        """Check if it is worthwhile rebalancing."""
        raise NotImplementedError
