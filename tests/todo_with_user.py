from generic.conditions.eq import eq
from generic.fields.foregin_key import ForeignKey
from generic.fields.serial import Serial
from generic.fields.timestamp import Timestamp
from generic.fields.varchar import Varchar
from generic.table import Table
from postgres.pg_connection import Postgres


class UserTable(Table):
    id = Serial('id', primary_key=True, nullable=False)
    email = Varchar('email', 255, nullable=False)
    password = Varchar('password', 255, nullable=False)
    created_at = Timestamp('created_at', auto_now_add=True, nullable=False)

    class Meta:
        table_name = 'users'


class TodoTable(Table):
    id = Serial('id', primary_key=True, nullable=False)
    title = Varchar('title', 255, nullable=False)
    user_id = ForeignKey('user_id', UserTable.id, nullable=False)
    created_at = Timestamp('created_at', auto_now_add=True, nullable=False)

    class Meta:
        table_name = 'todos'


db = Postgres('postgresql://localhost:5432', [
    UserTable,
    TodoTable,
])

print(db.create_tables_from_schema())

query_user = db.select().from_table(UserTable).where(eq(UserTable.id, 1)).execute()
print(query_user)

query_user_with_custom_select = db.select({
    "bilau_id": UserTable.id,
}).from_table(UserTable).where(eq(UserTable.id, 1)).execute()
print(query_user_with_custom_select)

query_all_todos = db.select().from_table(TodoTable).execute()
print(query_all_todos)

query_all_todos_with_pagination = db.select().from_table(TodoTable).limit(10).offset(0).execute()
print(query_all_todos_with_pagination)

insert_user = db.insert().into(UserTable).values({
    'email': 'caio@gmail.com',
    'password': '123456',
}).execute()
print(insert_user)
