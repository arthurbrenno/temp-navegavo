import typing
from .services import ScreenChatService


async def service_cls_factory() -> typing.Type[ScreenChatService]:
    return ScreenChatService
