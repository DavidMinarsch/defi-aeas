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

"""This module contains the handlers of the 'capital_allocation' skill."""

from typing import Any, Callable, Dict, List, Tuple, cast
from urllib.parse import parse_qs, urlparse

from aea.protocols.base import Message
from aea.skills.base import Handler

# pylint: disable=import-error,no-name-in-module
from packages.defi_aeas.skills.capital_allocation.dialogues import (
    HttpDialogue,
    HttpDialogues,
)
from packages.defi_aeas.skills.capital_allocation.strategy import Strategy
from packages.defi_aeas.skills.capital_allocation.tokens import Tokens
from packages.defi_aeas.skills.capital_allocation.transactions import Transactions
from packages.fetchai.protocols.http.message import HttpMessage


# pylint: enable=import-error,no-name-in-module


class HttpHandler(Handler):
    """This implements the echo handler."""

    SUPPORTED_PROTOCOL = HttpMessage.protocol_id

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize handler."""
        super().__init__(*args, **kwargs)
        self.request_handlers: Dict[
            Tuple[str, str],
            Callable[[Dict[str, List[str]], bytes], Tuple[bytes, str, int]],
        ] = {
            ("get", "/agent/status"): self._get_status,
            ("get", "/agent/name"): self._get_name,
            ("get", "transactions"): self._get_transactions,
            ("get", "tokens"): self._get_tokens,
            ("get", "whitelist"): self._get_whitelist,
        }

    def setup(self) -> None:
        """
        Implement the setup.

        :return: None
        """

    def handle(self, message: Message) -> None:
        """
        Implement the reaction to an envelope.

        :param message: the message
        :return: None
        """
        http_msg = cast(HttpMessage, message)

        # recover dialogue
        http_dialogues = cast(HttpDialogues, self.context.http_dialogues)
        http_dialogue = cast(HttpDialogue, http_dialogues.update(http_msg))
        if http_dialogue is None:
            self._handle_unidentified_dialogue(http_msg)
            return

        # handle message
        if http_msg.performative == HttpMessage.Performative.REQUEST:
            self._handle_request(http_msg, http_dialogue)
        else:
            self._handle_invalid(http_msg, http_dialogue)

    def _handle_unidentified_dialogue(self, http_msg: HttpMessage) -> None:
        """
        Handle an unidentified dialogue.

        :param http_msg: the message
        """
        self.context.logger.info(
            "received invalid http message={}, unidentified dialogue.".format(http_msg)
        )

    def _handle_request(
        self, http_msg: HttpMessage, http_dialogue: HttpDialogue
    ) -> None:
        """
        Handle a Http request.

        :param http_msg: the http message
        :param http_dialogue: the http dialogue
        :return: None
        """
        self.context.logger.info(
            "received http request with method={}, url={} and body={!r}".format(
                http_msg.method, http_msg.url, http_msg.body,
            )
        )
        parsed = urlparse(http_msg.url)
        query = parse_qs(parsed.query)
        request_handler = self.request_handlers.get(
            (http_msg.method, parsed.path), self._not_found
        )
        body, status_text, status_code = request_handler(query, http_msg.body)
        http_response = http_dialogue.reply(
            performative=HttpMessage.Performative.RESPONSE,
            target_message=http_msg,
            version=http_msg.version,
            status_code=status_code,
            status_text=status_text,
            headers="Content-Type: text/html",
            body=body,
        )
        self.context.logger.info("responding with: {}".format(http_response))
        self.context.outbox.put_message(message=http_response)

    def _handle_invalid(
        self, http_msg: HttpMessage, http_dialogue: HttpDialogue
    ) -> None:
        """
        Handle an invalid http message.

        :param http_msg: the http message
        :param http_dialogue: the http dialogue
        :return: None
        """
        self.context.logger.warning(
            "cannot handle http message of performative={} in dialogue={}.".format(
                http_msg.performative, http_dialogue
            )
        )

    def teardown(self) -> None:
        """
        Implement the handler teardown.

        :return: None
        """

    @staticmethod
    def _not_found(
        _query: Dict[str, List[str]], _body: bytes
    ) -> Tuple[bytes, str, int]:
        """Not found response."""
        return b"", "Resource not found", 404

    def _get_status(
        self, _query: Dict[str, List[str]], _body: bytes
    ) -> Tuple[bytes, str, int]:
        """Status response."""
        return (
            f"{cast(Strategy, self.context.strategy).agent_status}".encode("utf-8"),
            "Success",
            200,
        )

    def _get_name(
        self, _query: Dict[str, List[str]], _body: bytes
    ) -> Tuple[bytes, str, int]:
        """Name response."""
        return (
            f"{self.context.agent_name}".encode("utf-8"),
            "Success",
            200,
        )

    def _get_transactions(
        self, _query: Dict[str, List[str]], _body: bytes
    ) -> Tuple[bytes, str, int]:
        """Transactions response."""
        transactions = cast(Transactions, self.context.transactions)
        result = transactions.to_json().encode("utf-8")
        return result, "Success", 200

    def _get_tokens(
        self, _query: Dict[str, List[str]], _body: bytes
    ) -> Tuple[bytes, str, int]:
        """Tokens response."""
        tokens = cast(Tokens, self.context.tokens)
        result = tokens.to_json().encode("utf-8")
        return result, "Success", 200

    def _get_whitelist(
        self, _query: Dict[str, List[str]], _body: bytes
    ) -> Tuple[bytes, str, int]:
        """Tokens whitelist response."""
        return (
            f"{cast(Strategy, self.context.strategy).token_whitelist}".encode("utf-8"),
            "Success",
            200,
        )
