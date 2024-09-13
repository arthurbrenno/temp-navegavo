import msgspec
import typing
from llama_index.core.base.llms.types import ChatMessage


class ScreenInfoRequest(msgspec.Struct):
    messages: typing.Annotated[
        typing.List[ChatMessage],
        msgspec.Meta(title="Messages", description="A list of messages to chat with"),
    ]

    b64_image: typing.Annotated[
        typing.Optional[str],
        msgspec.Meta(
            title="Base 64 Encoded Image",
            description="The base 64 encoded image to send to the LLM",
        ),
    ]
