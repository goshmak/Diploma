class EntityError(Exception):
    pass


class UserError(EntityError):
    pass


class NotificationError(EntityError):
    pass


class UserEmailInvalidError(UserError):
    pass


class NotifEmptySubjectError(NotificationError):
    pass


class NotifEmptyBodyError(NotificationError):
    pass
