import typing

from navegavo.base import AsyncService
from openai import OpenAI
from .services import TranscriptionsService


async def client_factory() -> OpenAI:
    return OpenAI()


async def service_cls_factory() -> typing.Type[AsyncService[str]]:
    return TranscriptionsService
