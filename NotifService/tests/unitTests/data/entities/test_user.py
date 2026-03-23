from uuid import uuid4, UUID
from datetime import datetime

import pytest

from notifservice.data.entities.user import User
from notifservice.data.errors import UserEmailInvalidError


def makeUser(
    *,
    id: UUID | None = None,
    createdAt: datetime | None = None,
    updatedAt: datetime | None = None,
    email: str = "dog@dog.dog",
    messengerID: str = "id:88005553535",
    is_email: bool = True,
    is_messenger: bool = True,
) -> User:
    return User(
        id=id or uuid4(),
        createdAt=createdAt or datetime.now(),
        updatedAt=updatedAt or datetime.now(),
        email=email,
        messengerID=messengerID,
        is_email=is_email,
        is_messenger=is_messenger,
    )


def testValidUser():
    testUser = makeUser()
    assert isinstance(testUser.id, UUID)


def testInvalidEmail():
    with pytest.raises(UserEmailInvalidError):
        testUser = makeUser(email="dog&dog.dog")
