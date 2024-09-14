from __future__ import annotations

import typing

from litestar import Controller, MediaType, post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body, Dependency
from litestar.datastructures import UploadFile

from .di import client_factory, service_factory
from .schema import TranscriptionResponse
from .services import TranscriptionsService
from openai import OpenAI


class TranscriptionsController(Controller):
    path = "/v1/transcriptions"
    dependencies = {
        "client": Provide(client_factory),
        "service": Provide(service_factory),
    }

    @post(path="/", media_type=MediaType.TEXT)
    async def get_transcription(
        self,
        data: typing.Annotated[
            UploadFile, Body(media_type=RequestEncodingType.MULTI_PART)
        ],
        client: typing.Annotated[OpenAI, Dependency(skip_validation=True)],
        service: typing.Annotated[
            typing.Type[TranscriptionsService], Dependency(skip_validation=True)
        ],
    ) -> TranscriptionResponse:
        use_case = service(client=client, audio_file=data)
        transcription: str = await use_case.execute()
        return TranscriptionResponse(transcription=transcription)
