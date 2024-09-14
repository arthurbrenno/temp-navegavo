from __future__ import annotations

import msgspec
import typing
from openai.types.completion import Completion


class ScreenInfoResponse(msgspec.Struct):
    response: typing.Annotated[
        Completion,
        msgspec.Meta(title="Response", description="The response from the LLM."),
    ]
