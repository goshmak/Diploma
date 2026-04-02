from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

from notifservice.data.errors import NotifEmptySubjectError, NotifEmptyBodyError
from notifservice.data.enums.notifType import NotifType
from notifservice.data.enums.notifStatus import NotifStatus
from notifservice.data.valueObjects.notifContent import NotifContent


@dataclass(frozen=True)
class Notification:
    id: UUID
    createdAt: datetime
    notifType: NotifType
    userID: UUID
    notifStatus: NotifStatus
    notifContent: NotifContent

    def __post_init__(self) -> None:
        self.check()

    def check(self):
        if not self.notifContent.subject:
            raise NotifEmptySubjectError("Отсутствует тема уведомления")
        if not self.notifContent.body:
            raise NotifEmptyBodyError("Отсутствует тело уведомления")
