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

"""
This module contains the classes required for dialogue management.

- HttpDialogue: The dialogue class maintains state of a dialogue of type http and manages it.
- HttpDialogues: The dialogues class keeps track of all dialogues of type http.
"""

from aea.protocols.base import Address, Message
from aea.protocols.dialogue.base import Dialogue as BaseDialogue
from aea.skills.base import Model

# pylint: disable=import-error,no-name-in-module
from packages.fetchai.protocols.http.dialogues import HttpDialogue as BaseHttpDialogue
from packages.fetchai.protocols.http.dialogues import HttpDialogues as BaseHttpDialogues


# pylint: enable=import-error,no-name-in-module


HttpDialogue = BaseHttpDialogue


class HttpDialogues(Model, BaseHttpDialogues):
    """The dialogues class keeps track of all dialogues."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize dialogues.

        :return: None
        """
        Model.__init__(self, **kwargs)

        def role_from_first_message(  # pylint: disable=unused-argument
            message: Message, receiver_address: Address
        ) -> BaseDialogue.Role:
            """
            Infer the role of the agent from an incoming/outgoing first message.

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            return BaseHttpDialogue.Role.SERVER

        BaseHttpDialogues.__init__(
            self,
            self_address=self.context.agent_address,
            role_from_first_message=role_from_first_message,
        )
