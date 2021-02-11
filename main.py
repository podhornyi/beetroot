from sqlalchemy.orm.session import SessionTransaction

from db.models import User#, UserData, RelRoomUser, Message, Room
from db.models import Room
from db import session_scope


print('Start program')

with session_scope() as session:
    session\
        .query(User).delete()
    session\
        .query(Room).delete()


# with session_scope() as session:
#     kola = User(nickname='kola', password='123')
#     ivan = User(nickname='ivan', password='123')
#     olya = User(nickname='olya', password='123')
#     kola_data = UserData(
#         first_name='Kola',
#         last_name='Nikolaevich',
#         profile_picture='alkhcsn.jpeg',
#     )
#     ivan_data = UserData(
#         first_name='Ivan',
#         last_name='Ivanovich',
#         profile_picture='alkhcsn.jpeg',
#     )
#     olya_data = UserData(
#         first_name='Tania',
#         last_name='Nikolaevich',
#         profile_picture='alkhcsn.jpeg',
#     )
#     kola.user_data = kola_data
#     ivan.user_data = ivan_data
#     olya.user_data = olya_data
#     session.add_all([olya, ivan, kola])





