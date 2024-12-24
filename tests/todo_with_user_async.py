import asyncio
from operator import eq
from uuid import uuid4

from generic.fields.serial import Serial
from generic.fields.timestamp import Timestamp
from generic.fields.varchar import Varchar
from generic.table import Table
from postgres.pg_connection import Postgres


class UserTable(Table):
    id = Serial('id').primary_key().not_null()
    pid = Varchar('pid', 255).default(uuid4().__str__).not_null()
    email = Varchar('email', 255).not_null()
    password = Varchar('password', 255).not_null()
    created_at = Timestamp('created_at', auto_now_add=True).not_null()

    class Meta:
        table_name = 'users'


db = Postgres('postgresql://root:rootpwd@localhost:5432/test', [
    UserTable,
])


async def main():
    await db.connect()

    result = await db.select().from_table(UserTable).where(eq(UserTable.id, 1)).execute()

    if len(result) > 0:
        user = result[0]
        print(user)

    print('Done')


if __name__ == "__main__":
    asyncio.run(main())
