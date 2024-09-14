import msgspec
import typing


class ScreenInfoRequest(msgspec.Struct):
    messages: typing.Annotated[
        typing.List[typing.Dict[str, typing.Any]],
        msgspec.Meta(title="Messages", description="A list of messages to chat with"),
    ]
