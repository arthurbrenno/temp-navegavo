import typing

from openai.types.completion import Completion

from navegavo.base import AsyncService

from .services import ScreenChatService


async def service_cls_factory() -> typing.Type[AsyncService[Completion]]:
    return ScreenChatService
