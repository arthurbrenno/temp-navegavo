import typing

from litestar import Controller, Litestar, MediaType, post
from litestar.datastructures import UploadFile
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body, Dependency
from llama_index.core.multi_modal_llms.base import MultiModalLLM

from .di import llm_factory
from .schema import ScreenInfo


class NavegavoController(Controller):
    path = "/v1"
    dependencies = {"llm": Provide(llm_factory)}

    @post(path="/screen-info", media_type=MediaType.TEXT)
    async def get_screen_info(
        self,
        data: typing.Annotated[
            UploadFile, Body(media_type=RequestEncodingType.MULTI_PART)
        ],
        llm: typing.Annotated[MultiModalLLM, Dependency(skip_validation=True)]
    ) -> ScreenInfo:
        contents: bytes = await data.read()
        llm.
        return ScreenInfo(description="Temp.")
