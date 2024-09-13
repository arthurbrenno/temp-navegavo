import typing

from llama_index.core.base.llms.types import ChatResponse
from llama_index.core.multi_modal_llms.base import MultiModalLLM
from llama_index.multi_modal_llms.gemini import GeminiMultiModal  # type: ignore

from navegavo.base import AsyncService

from .services import ScreenChatService


async def llm_factory() -> MultiModalLLM:
    return GeminiMultiModal()


async def service_factory() -> typing.Type[AsyncService[ChatResponse]]:
    return ScreenChatService
