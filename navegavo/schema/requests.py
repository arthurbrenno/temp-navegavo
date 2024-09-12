import msgspec
import typing
from llama_index.core.base.llms.types import ChatMessage

class ScreenHelpRequest(msgspec.Struct):
    messages: typing.Annotated[
        typing.List[ChatMessage],
        msgspec.Meta(title="", description="")
    ]