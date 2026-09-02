from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.session import Base


class QuestionOption(Base):
    __tablename__ = "question_options"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    option_key: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    option_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    display_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    question = relationship(
        "Question",
        back_populates="options",
    )