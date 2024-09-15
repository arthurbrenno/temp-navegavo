from __future__ import annotations

import typing

from litestar import Controller, post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body, Dependency
from litestar.datastructures import UploadFile
from litestar.config.response_cache import CACHE_FOREVER

from .di import client_factory, service_cls_factory
from .schema import TranscriptionResponse
from .services import TranscriptionsService
from openai import OpenAI


class TranscriptionsController(Controller):
    path = "/v1/transcriptions"
    dependencies = {
        "client": Provide(client_factory),
        "service": Provide(service_cls_factory),
    }

    @post(path="/", cache=False)
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
