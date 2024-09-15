import typing

from openai import OpenAI
from openai.types.completion import Completion

from navegavo.base import AsyncService

from .services import ScreenChatService


def client_factory() -> OpenAI:
    return OpenAI()


async def service_cls_factory() -> typing.Type[AsyncService[Completion]]:
    return ScreenChatService
