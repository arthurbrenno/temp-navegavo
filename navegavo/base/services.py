import typing

from navegavo.typing import T_co


@typing.runtime_checkable
class AsyncService(typing.Protocol, typing.Generic[T_co]):
    async def execute(self) -> T_co: ...
