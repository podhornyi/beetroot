from sqlalchemy import (
    Column, Integer, String,
    ForeignKey, DateTime, orm
)
from web.db import Base

from datetime import datetime


class BaseTable(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, nullable=False)

    create_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    update_at = Column(DateTime, nullable=True)
    delete_at = Column(DateTime, nullable=True)


class User(BaseTable):
    __tablename__ = 'users'

    nickname = Column(String(30), unique=True, nullable=False)


class Message(BaseTable):
    __tablename__ = 'messages'

    text = Column(String(50), unique=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = orm.relationship(
        'User',
        backref='messages',
        lazy='joined'
    )


Base.metadata.create_all()
