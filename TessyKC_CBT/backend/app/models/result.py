from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.session import Base


class Result(Base):
    __tablename__ = "results"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    session_id: Mapped[int] = mapped_column(
        ForeignKey("exam_sessions.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    score: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    percentage: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    correct_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    wrong_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    unanswered_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    time_used: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    session = relationship(
        "ExamSession",
        back_populates="result",
    )