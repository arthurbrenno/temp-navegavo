import typing

import msgspec
import tempfile
from litestar.datastructures import UploadFile
from openai import OpenAI


class TranscriptionsService(msgspec.Struct, kw_only=True):
    client: typing.Annotated[
        OpenAI, msgspec.Meta(title="Client responsible for transcriptions")
    ]

    audio_file: typing.Annotated[
        UploadFile,
        msgspec.Meta(
            title="Upload File", description="The uploaded audio file to transcribe"
        ),
    ]

    async def execute(self) -> str:
        # Get the original filename and extension from the uploaded file
        original_filename = self.audio_file.filename
        file_extension = original_filename.split('.')[-1]

        # Ensure the temporary file has the correct extension
        with tempfile.NamedTemporaryFile(suffix=f'.{file_extension}', mode="wb", delete=False) as tmp:
            tmp.write(await self.audio_file.read())
            tmp.seek(0)  # Ensure we start reading from the beginning of the file
            
            # Open the file for reading as bytes for the transcription request
            with open(tmp.name, "rb") as audio:
                transcription = self.client.audio.transcriptions.create(
                    file=audio,  # Pass the file object
                    model="whisper-1",
                    response_format="json",
                    language="pt",
                )

            # Optionally delete the file after using
            return transcription.text
