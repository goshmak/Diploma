from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass(frozen=True)
class NotifContent:
    subject: str
    body: str
    assignment_id: Optional[UUID] = None  # ID задания
    submission_id: Optional[UUID] = None  # ID решения
    deadline: Optional[str] = None  # Дата дедлайна
    grade: Optional[int] = None  # Оценка за решение
    feedback: Optional[str] = None  # Отзыв преподавателя
