from sqlalchemy_train.sql_queries import engine
from db_connection import DBConnection
from sqlalchemy import func, desc
from sqlalchemy_train.sql_queries.models import User, News, Role
import json
from datetime import datetime


# TASK1  Получить всех пользователей-авторов с рейтингом больше 5

# with DBConnection(engine) as session:
#     list_authors = session.query(User.id, User.last_name, User.role_id, User.rating).filter(
#         User.role_id == 3, User.rating > 5
#     ).all()
#
#     for author in list_authors:
#         print(author.id, author.last_name, author.role_id, author.rating)

#=====================================================================================================================

# TASK2 Получить все новости, которые не удалены и не модерированы

# with DBConnection(engine) as session:
#     news_list = session.query(News.title, News.moderated, News.deleted, News.author_id).filter(
#         News.moderated == 0, News.deleted == 0
#     ).all()
#
#     response_data = [
#         {
#             "title": news.title,
#             "moderated": news.moderated,
#             "deleted": news.deleted,
#             "author_id": news.author_id,
#         }
#         for news in news_list
#     ]
#
#     print(json.dumps(response_data, indent=4)) # indent : количество отступов

#===========================================================================================================
# TASK3  Найти всех пользователей, зарегистрированных в 2022 году

# with DBConnection(engine) as session:
#     users_22 = session.query(User.last_name, User.created_at).filter(
#         User.created_at.between(datetime(2022, 1, 1), datetime(2022, 12, 31))
#
#     ).all()
#
#     response_data = [
#         {
#             "last_name": user.last_name,
#             "created_at": datetime.strftime(user.created_at, '%Y-%m-%d %H:%M:%S')
#         }
#         for user in users_22
#     ]
#
#     print(json.dumps(response_data, indent=4))

#===========================================================================================================

# TASK4 Получить список всех пользователей с их ролями

# with DBConnection(engine) as session:
#     all_users_with_role = session.query(
#         User.last_name,
#         User.email,
#         Role.name.label("role_name")
#     ).join(User.role).all()
#
#     for user in all_users_with_role:
#         print(user.last_name, user.email, user.role_name)

#===========================================================================================================

# TASK4   Найти автора с наибольшим количеством новостей выводить дополнительно имя роли авторов

# with DBConnection(engine) as session:
#     author = session.query(User.last_name,
#                            User.email,
#                            Role.name.label('name_role'),
#                            User.rating,
#                            func.count().label('cn')).join(
#         User.role).join(User.news).group_by(User.last_name,
#                                             User.email,
#                                             Role.name,
#                                             User.rating).order_by(desc(func.count())).first()
#
#     print(author)