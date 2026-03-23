from enum import Enum


class NotifStatus(str, Enum):
    Pending = "Pending"
    Sent = "Sent"
    Failed = "Failed"
