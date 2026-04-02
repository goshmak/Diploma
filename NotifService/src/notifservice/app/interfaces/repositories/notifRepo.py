from typing import Protocol
from uuid import UUID

from notifservice.data.entities.notification import Notification


class NotifRepo(Protocol):
    async def create(self, notif: Notification) -> Notification | None: ...
    async def delete(self, id: UUID) -> Notification | None: ...
    async def getByID(self, id: UUID) -> Notification | None: ...
