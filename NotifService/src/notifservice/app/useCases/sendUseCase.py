from notifservice.app.interfaces.emailSender import EmailSender
from notifservice.app.interfaces.unitOfWork import UnitOfWork


class EmailSendUseCase:
    def __init__(self, es: EmailSender, uow: UnitOfWork) -> None:
        self._es = es
        self._uow = uow

    async def execute(self) -> None:
        ...