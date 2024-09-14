import typing

import msgspec
from llama_index.core.base.llms.types import ChatResponse
import tempfile
from litestar.datastructures import UploadFile
from groq import Groq


class TranscriptionsService(msgspec.Struct, kw_only=True):
    client: typing.Annotated[
        Groq, msgspec.Meta(title="Client responsible for transcriptions")
    ]

    audio_file: typing.Annotated[
        UploadFile,
        msgspec.Meta(
            title="Upload File", description="The uploaded audio file to transcribe"
        ),
    ]

    async def execute(self) -> str:
        with tempfile.NamedTemporaryFile(mode="wb", delete=True) as tmp:
            tmp.write(await self.audio_file.read())
            tmp_path = tmp.name
            transcription = self.client.audio.transcriptions.create(
                file=(tmp_path, tmp.read()),
                model="whisper-large-v3",
                response_format="json",
                language="en",
            )
            return transcription.text
