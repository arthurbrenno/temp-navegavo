from __future__ import annotations

import typing

from litestar import Controller, MediaType, post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body, Dependency
from llama_index.core.base.llms.types import ChatResponse
from llama_index.core.multi_modal_llms.base import MultiModalLLM

from .di import llm_factory, service_cls_factory
from .schema import ScreenInfoRequest, ScreenInfoResponse
from .services import ScreenChatService


class ScreenChatController(Controller):
    path = "/v1/screen-info"
    dependencies = {
        "llm": Provide(llm_factory),
        "service": Provide(service_cls_factory),
    }

    @post(path="/", media_type=MediaType.TEXT)
    async def get_screen_info(
        self,
        data: typing.Annotated[
            ScreenInfoRequest, Body(media_type=RequestEncodingType.JSON)
        ],
        llm: typing.Annotated[MultiModalLLM, Dependency(skip_validation=True)],
        service: typing.Annotated[
            typing.Type[ScreenChatService], Dependency(skip_validation=True)
        ],
    ) -> ScreenInfoResponse:
        use_case = service(llm=llm, messages=data.messages)
        response: ChatResponse = await use_case.execute()
        return ScreenInfoResponse(response=response)
