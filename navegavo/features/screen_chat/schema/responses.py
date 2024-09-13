from __future__ import annotations

import msgspec
import typing
from llama_index.core.base.llms.types import ChatResponse


class ScreenInfoResponse(msgspec.Struct):
    response: typing.Annotated[
        ChatResponse,
        msgspec.Meta(title="Response", description="The response from the LLM."),
    ]
