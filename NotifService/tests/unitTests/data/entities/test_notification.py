from uuid import uuid4, UUID
from datetime import datetime

import pytest

from notifservice.data.entities.notification import Notification
from notifservice.data.valueObjects.notifContent import NotifContent
from notifservice.data.enums.notifType import NotifType
from notifservice.data.enums.notifStatus import NotifStatus
from notifservice.data.errors import NotifEmptySubjectError, NotifEmptyBodyError


def makeNotification(
    *,
    id: UUID | None = None,
    createdAt: datetime | None = None,
    notifType: NotifType = NotifType.NewTask,
    userID: UUID | None = None,
    notifStatus: NotifStatus = NotifStatus.Sent,
    contentSubject: str = "BigShlyopa",
    contentBody: str = "BigBrotherIsEatinngPelmenis",
) -> Notification:
    return Notification(
        id=id or uuid4(),
        createdAt=createdAt or datetime.now(),
        notifType=notifType,
        userID=userID or uuid4(),
        notifStatus=notifStatus,
        notifContent=NotifContent(subject=contentSubject, body=contentBody),
    )


def testValidNotification():
    testNotif = makeNotification()
    assert isinstance(testNotif.id, UUID)


def testEmptySubj():
    with pytest.raises(NotifEmptySubjectError):
        testNotif = makeNotification(contentSubject="")


def testEmptyBody():
    with pytest.raises(NotifEmptyBodyError):
        testNotif = makeNotification(contentBody="")
