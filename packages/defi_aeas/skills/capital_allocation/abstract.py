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

import json
from typing import Dict, NamedTuple, Optional, Type

from aea.skills.base import Model


OnChainItemId = str  # Address or transaction hash


OnChainItem = NamedTuple


class OnChainItemCollection(Model):
    """Representation of onchain collection."""

    item_class: Type[OnChainItem]

    def __init__(self, **kwargs) -> None:
        """
        Initialize dialogues.

        :return: None
        """
        Model.__init__(self, **kwargs)
        self._items: Dict[OnChainItemId, OnChainItem] = {}

    def add(self, item: OnChainItem) -> None:
        """
        Add an item.

        :param item: the on chain item
        :return: None
        """
        if not isinstance(item, self.item_class):
            raise ValueError(
                f"Item type={type(item)} is not a valid type for collection {self.__class__.__name__}"
            )
        onchain_id = getattr(item, "onchain_id", None)
        if onchain_id is None:
            raise ValueError(f"Idem={item} does not have an `onchain_id`.")
        if onchain_id in self._items:
            raise ValueError(f"Item with onchain_id={onchain_id} already registered.")
        self._items[onchain_id] = item

    def get(self, onchain_id: OnChainItemId) -> Optional[OnChainItem]:
        """
        Get a item based on its onchain_id.

        :param onchain_id: the onchain_id of the item.
        :return: the item if it exists.
        """
        return self._items.get(onchain_id, None)

    def to_json(self) -> str:
        """Get the json representation of the data."""
        result = json.dumps([dict(value._asdict()) for value in self._items.values()])
        return result
