from __future__ import annotations

import typing

from litestar import Controller, post
from litestar.config.response_cache import CACHE_FOREVER
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body, Dependency
from openai import OpenAI

from .di import client_factory, service_cls_factory
from .schema import TextToSpeechRequest
from .services import TextToSpeechService


class TextToSpeechController(Controller):
    path = "/v1/text-to-speech"
    dependencies = {
        "client": Provide(client_factory),
        "service": Provide(service_cls_factory),
    }

    @post(path="/", cache=CACHE_FOREVER)
    async def get_screen_info(
        self,
        data: typing.Annotated[
            TextToSpeechRequest, Body(media_type=RequestEncodingType.JSON)
        ],
        client: typing.Annotated[
            OpenAI,
            Dependency(skip_validation=True),
        ],
        service: typing.Annotated[
            typing.Type[TextToSpeechService], Dependency(skip_validation=True)
        ],
    ) -> dict:
        use_case = service(client=client, text=data.text)
        return {"audio": await use_case.execute()}
