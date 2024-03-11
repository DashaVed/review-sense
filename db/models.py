from typing import List
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    name: Mapped[str]
    reviews: Mapped[List["Review"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"


class Review(Base):

    __tablename__ = "review"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    mood: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def __repr__(self) -> str:
        return f"Review(id={self.id!r}, text={self.text!r}, mood={self.mood!r})"
