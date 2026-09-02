from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.session import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    examination_id: Mapped[int] = mapped_column(
        ForeignKey("examinations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id"),
        nullable=False,
        index=True,
    )

    topic_id: Mapped[int] = mapped_column(
        ForeignKey("topics.id"),
        nullable=False,
        index=True,
    )

    question_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    question_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    correct_option: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    difficulty: Mapped[str] = mapped_column(
        String(30),
        default="medium",
        nullable=False,
    )

    marks: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="draft",
        nullable=False,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        default=1,
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

    examination = relationship(
        "Examination",
        back_populates="questions",
    )

    subject = relationship("Subject")

    topic = relationship(
        "Topic",
        back_populates="questions",
    )

    options = relationship(
        "QuestionOption",
        back_populates="question",
        cascade="all, delete-orphan",
    )

    solution = relationship(
        "Solution",
        back_populates="question",
        uselist=False,
        cascade="all, delete-orphan",
    )