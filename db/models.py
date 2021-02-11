

from sqlalchemy import (
    Column, Integer, String,
    ForeignKey, DateTime, orm, UniqueConstraint,
    PrimaryKeyConstraint
)
from db import Base, engine

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
    password = Column(String, nullable=False)

    # user_data = orm.relationship(
    #     'UserData',
    #     backref='user_data',
    #     uselist=False
    # )

    # outbox_messages = orm.relationship(
    #     'Message',
    #     backref='outbox'
    # )
    #
    # inbox_messages = orm.relationship(
    #     'Message',
    #     backref='inbox'
    # )

    # rooms = orm.relationship(
    #     'Room',
    #     backref='users',
    #     secondary='RelRoomUser'
    # )

#
# class UserData(BaseTable):
#
#     __tablename__ = 'users_data'
#
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     first_name = Column(String(30))
#     last_name = Column(String(30))
#     profile_picture = Column(String)
#
#     __table_args__ = (
#         UniqueConstraint(user_id),
#     )


# class Message(BaseTable):
#
#     __tablename__ = 'messages'
#
#     message = Column(String)
#     sender = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     recipient = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#
#     user = orm.relationship('User', backref='sent_messages')
#     # recipient_rel = orm.relationship('User')
#

class Room(BaseTable):

    __tablename__ = 'rooms'

    name = Column(String(50), unique=True)
    users = orm.relationship(
        'RelRoomUser',
        backref='rooms',
        secondary='RelRoomUser'
    )


class RelRoomUser(Base):
    __tablename__ = 'rel_room_users'

    room_id = Column(Integer, ForeignKey('rooms.id', ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    __table_args__ = (
        PrimaryKeyConstraint(room_id, user_id),
    )


Base.metadata.create_all()
