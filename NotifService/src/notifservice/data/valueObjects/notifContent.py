from dataclasses import dataclass


@dataclass(frozen=True)
class NotifContent:
    subject: str
    body: str
