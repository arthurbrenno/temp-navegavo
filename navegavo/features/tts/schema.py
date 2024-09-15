import msgspec
import typing


class TextToSpeechRequest(msgspec.Struct):
    text: typing.Annotated[
        str,
        msgspec.Meta(title="Text", description="Text to be converted to speech"),
    ]
