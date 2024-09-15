from __future__ import annotations

import msgspec
import typing


class TranscriptionResponse(msgspec.Struct):
    transcription: typing.Annotated[
        str,
        msgspec.Meta(
            title="Transcription", description="Transcribed text from the audio file"
        ),
    ]
