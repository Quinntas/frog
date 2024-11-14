from abc import ABC
from typing import List, Optional, Any

import aiopg

from generic.connection import Connection
from generic.typings import TableType


class Postgres(Connection, ABC):
    def __init__(self, uri: str, schema: Optional[List[TableType]] = None):
        super().__init__(uri, schema or [])
        self.connection = None

    async def connect(self):
        if not self.connection:
            self.connection = await aiopg.create_pool(self.uri)

    async def query(self, query: str, parameters: tuple[Any] = ()) -> List[tuple]:
        if not self.connection:
            raise RuntimeError("Database not connected. Call connect() first.")

        async with self.connection.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(query, parameters)
                return await cur.fetchall()

    async def transaction(self):
        if not self.connection:
            raise RuntimeError("Database not connected. Call connect() first.")

        conn = await self.connection.acquire()
        trans = await conn.begin()

        try:
            yield conn
            await trans.commit()
        except Exception:
            await trans.rollback()
            raise
        finally:
            await self.connection.release(conn)

    async def execute(self, query: str, parameters: tuple[Any] = ()):
        if not self.connection:
            raise RuntimeError("Database not connected. Call connect() first.")

        async with self.connection.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(query, parameters)

    async def close(self):
        if self.connection:
            await self.connection.close()
            self.connection = None
