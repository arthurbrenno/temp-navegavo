from __future__ import annotations

import typing

from litestar import Controller, post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body, Dependency
from litestar.config.response_cache import CACHE_FOREVER
from .di import service_cls_factory
from .schema import ScreenInfoRequest
from .services import ScreenChatService


class ScreenChatController(Controller):
    path = "/v1/screen-info"
    dependencies = {
        "service": Provide(service_cls_factory),
    }

    @post(path="/", cache=CACHE_FOREVER)
    async def get_screen_info(
        self,
        data: typing.Annotated[
            ScreenInfoRequest, Body(media_type=RequestEncodingType.JSON)
        ],
        service: typing.Annotated[
            typing.Type[ScreenChatService], Dependency(skip_validation=True)
        ],
    ) -> dict:
        use_case = service(messages=data.messages)
        return await use_case.execute()
