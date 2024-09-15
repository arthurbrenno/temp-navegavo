import msgspec
import typing
from openai.types.completion import Completion


class ScreenInfoRequest(msgspec.Struct):
    messages: typing.Annotated[
        typing.List[typing.Dict[str, typing.Any]],
        msgspec.Meta(title="Messages", description="A list of messages to chat with"),
    ]


class ScreenInfoResponse(msgspec.Struct):
    response: typing.Annotated[
        Completion,
        msgspec.Meta(title="Response", description="The response from the LLM."),
    ]
