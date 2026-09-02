from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.session import Base


class Examination(Base):
    __tablename__ = "examinations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    exam_body: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    exam_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id"),
        nullable=False,
        index=True,
    )

    paper: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    duration_minutes: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    question_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    total_marks: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_published: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    subject = relationship(
        "Subject",
        back_populates="examinations",
    )

    questions = relationship(
        "Question",
        back_populates="examination",
        cascade="all, delete-orphan",
    )

    sessions = relationship(
        "ExamSession",
        back_populates="examination",
    )