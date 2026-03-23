from enum import Enum


class NotifType(str, Enum):
    NewTask = "NewTask"
    SubmCreated = "SubmCreated"
    SubmChecked = "SubmChecked"
    Deadline = "Deadline"
