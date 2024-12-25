from abc import ABC
from typing import List, Optional, Any

import asyncpg

from generic.connection import Connection
from generic.typings import TableType


class AsyncPG(Connection, ABC):
    def __init__(self, uri: str, schema: Optional[List[TableType]] = None):
        super().__init__(uri, schema or [])
        self.pool = None

    async def connect(self):
        if self.pool:
            raise RuntimeError("Database already connected. Call close() first.")
        self.pool = await asyncpg.create_pool(self.uri)

    async def query(self, query: str, *args):
        if not self.pool:
            raise RuntimeError("Database not connected. Call connect() first.")

        async with self.pool.acquire() as conn:
            records = await conn.fetch(query, *args)
            return [dict(r) for r in records]

    async def transaction(self):
        if not self.pool:
            raise RuntimeError("Database not connected. Call connect() first.")

        async with self.pool.acquire() as conn:
            async with conn.transaction():
                yield conn

    async def execute(self, query: str, parameters: tuple[Any] = ()):
        if not self.pool:
            raise RuntimeError("Database not connected. Call connect() first.")

        async with self.pool.acquire() as conn:
            await conn.execute(query, *parameters)

    async def close(self):
        if self.pool:
            await self.pool.close()
            self.pool = None
