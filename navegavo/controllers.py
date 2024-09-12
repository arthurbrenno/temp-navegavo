import typing

from litestar import Controller, MediaType, post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body, Dependency
from llama_index.core.base.llms.types import ChatResponse
from llama_index.core.multi_modal_llms.base import MultiModalLLM

from .di import llm_factory
from .schema import ScreenInfoRequest, ScreenInfoResponse


class NavegavoController(Controller):
    path = "/v1"
    dependencies = {"llm": Provide(llm_factory)}

    @post(path="/screen-info", media_type=MediaType.TEXT)
    async def get_screen_info(
        self,
        data: typing.Annotated[
            ScreenInfoRequest, Body(media_type=RequestEncodingType.MULTI_PART)
        ],
        llm: typing.Annotated[MultiModalLLM, Dependency(skip_validation=True)],
    ) -> ScreenInfoResponse:
        response: ChatResponse = await llm.achat(messages=data.messages)
        return ScreenInfoResponse(response=response)
