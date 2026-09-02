from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.session import Base


class ExamSession(Base):
    __tablename__ = "exam_sessions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    examination_id: Mapped[int] = mapped_column(
        ForeignKey("examinations.id"),
        nullable=False,
        index=True,
    )

    device_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    submitted_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="in_progress",
        nullable=False,
    )

    time_used: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    examination = relationship(
        "Examination",
        back_populates="sessions",
    )

    answers = relationship(
        "StudentAnswer",
        back_populates="session",
        cascade="all, delete-orphan",
    )

    result = relationship(
        "Result",
        back_populates="session",
        uselist=False,
        cascade="all, delete-orphan",
    )