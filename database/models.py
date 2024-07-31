from typing import List

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship, backref, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Band(Base):
    __tablename__ = "bands"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    album: Mapped[List["Album"]] = relationship(back_populates="band")
    song: Mapped[List["Song"]] = relationship(back_populates="band")

    def __str__(self):
        return self.name


class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    band_id: Mapped[int] = ForeignKey("Band.id")

    band: Mapped["Band"] = relationship(back_populates="album")
    song: Mapped[List["Song"]] = relationship(back_populates="album")

    def __str__(self):
        return self.name


class Song(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    tg_id: Mapped[str] = mapped_column(nullable=False)
    band_id: Mapped[int] = ForeignKey("Band.id")
    album_id: Mapped[int] = ForeignKey("Album.id")

    band: Mapped["Band"] = relationship(back_populates="song")
    album: Mapped["Album"] = relationship(back_populates="song")

