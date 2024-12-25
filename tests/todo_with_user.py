from uuid import uuid4

from connections.asyncpg_connection import Postgres
from generic.conditions.and_condition import and_condition
from generic.conditions.eq import eq
from generic.fields.foregin_key import ForeignKey
from generic.fields.serial import Serial
from generic.fields.timestamp import Timestamp
from generic.fields.varchar import Varchar
from generic.table import Table


class UserTable(Table):
    id = Serial('id').primary_key().not_null()
    pid = Varchar('pid', 255).default(uuid4().__str__).not_null()
    email = Varchar('email', 255).not_null()
    password = Varchar('password', 255).not_null()
    created_at = Timestamp('created_at', auto_now_add=True).not_null()

    class Meta:
        table_name = 'users'


class TodoTable(Table):
    id = Serial('id').primary_key().not_null()
    pid = Varchar('pid', 255).default(uuid4().__str__).not_null()
    title = Varchar('title', 255).not_null()
    user_id = ForeignKey('user_id', UserTable.id).not_null()
    created_at = Timestamp('created_at', auto_now_add=True).not_null()

    class Meta:
        table_name = 'todos'


db = Postgres('postgresql://localhost:5432', [
    UserTable,
    TodoTable,
])

print(db.create_tables_from_schema())

query_user = db.select().from_table(UserTable).where(eq(UserTable.id, 1)).execute()
print(query_user[0])

query_user_with_and = db.select().from_table(UserTable).where(and_condition(
    eq(UserTable.id, 1),
    eq(UserTable.email, 'caio@gmail.com'),
)).execute()
print(query_user_with_and)

query_user_with_custom_select = db.select({
    "bilau_id": UserTable.id,
}).from_table(UserTable).where(eq(UserTable.id, 1)).execute()
print(query_user_with_custom_select)

query_all_todos = db.select().from_table(TodoTable).execute()
print(query_all_todos)

query_all_todos_with_pagination = db.select().from_table(TodoTable).limit(10).offset(0).execute()
print(query_all_todos_with_pagination)

query_all_todos_with_join = db.select().from_table(TodoTable).right_join(
    UserTable, eq(TodoTable.user_id, UserTable.id)
).execute()
print(query_all_todos_with_join)

insert_user = db.insert().into(UserTable).values({
    'email': 'caio@gmail.com',
    'password': '123456',
}).execute()
print(insert_user)

update_user = db.update().table(UserTable).set(UserTable.email, 'caio2@mgial.com').where(eq(UserTable.id, 1)).execute()
print(update_user)
