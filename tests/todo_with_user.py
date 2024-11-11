from generic.conditions.eq import eq
from generic.fields.foregin_key import ForeignKey
from generic.fields.serial import Serial
from generic.fields.timestamp import Timestamp
from generic.fields.varchar import Varchar
from generic.table import Table
from postgres.pg_connection import Postgres


class UserTable(Table):
    id = Serial('id', primary_key=True)
    email = Varchar('email', 255)
    password = Varchar('password', 255)
    created_at = Timestamp('created_at', auto_now_add=True)

    class Meta:
        table_name = 'users'


class TodoTable(Table):
    id = Serial('id', primary_key=True)
    title = Varchar('title', 255)
    user_id = ForeignKey(UserTable, UserTable.id)
    created_at = Timestamp('created_at', auto_now_add=True)

    class Meta:
        table_name = 'todos'


db = Postgres('postgresql://localhost:5432')

query = db.select().from_table(UserTable).where(eq(UserTable.id, 1)).execute()

print(query)
