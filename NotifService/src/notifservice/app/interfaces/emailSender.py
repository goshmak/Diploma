from typing import Protocol


class EmailSender(Protocol):
    login: str
    password: str
    host: str
    port: int

    async def send(self, address: str) -> str: ...
