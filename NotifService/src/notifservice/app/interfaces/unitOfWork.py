from typing import Protocol

from notifservice.app.interfaces.repositories.notifRepo import NotifRepo
from notifservice.app.interfaces.repositories.userRepo import UserRepo


class UnitOfWork(Protocol):
    notif: NotifRepo
    user: UserRepo

    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc, tb): ...
    async def commit(self) -> None: ...
    async def rollBack(self) -> None: ...
