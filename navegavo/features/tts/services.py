import base64
import typing

import msgspec
from openai import OpenAI


class TextToSpeechService(msgspec.Struct, kw_only=True):
    client: typing.Annotated[
        OpenAI,
        msgspec.Meta(
            title="Client", description="OpenAI client to interact with the API"
        ),
    ]

    text: typing.Annotated[
        str,
        msgspec.Meta(title="Text", description="Text to be converted to speech"),
    ]

    async def execute(self) -> str:
        response = self.client.audio.speech.create(
            model="tts-1", voice="alloy", input=self.text
        )
        return base64.b64encode(await response.aread()).decode("utf-8")
