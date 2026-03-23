from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

from notifservice.data.errors import UserEmailInvalidError


@dataclass(frozen=True)
class User:
    id: UUID
    createdAt: datetime
    updatedAt: datetime
    email: str = ""
    messengerID: str = ""
    is_email: bool = False
    is_messenger: bool = False

    def __post_init__(self) -> None:
        self.check()

    def check(self):
        if "@" not in self.email:
            raise UserEmailInvalidError("Некорректный e-mail адрес")
