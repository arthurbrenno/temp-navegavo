import typing

from navegavo.base import AsyncService
from groq import Groq
from .services import TranscriptionsService


async def client_factory() -> Groq:
    return Groq()


async def service_cls_factory() -> typing.Type[AsyncService[str]]:
    return TranscriptionsService
