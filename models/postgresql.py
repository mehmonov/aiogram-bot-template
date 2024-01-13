from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user="postgres",
            password="1234",
            host="localhost",
            database="market"
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL,
            username varchar(255) NULL,
            telegram_id BIGINT NOT NULL UNIQUE,
            location varchar(255) NOT NULL,
            phone_number varchar(255) NOT NULL
        
        );
        """
        await self.execute(sql, execute=True)
    
    async def create_table_products(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price varchar(255) NOT NULL,
            amount varchar(255) NULL ,
           
            type varchar(255) NOT NULL,
            category varchar(255)  NOT NULL,  
            
            image varchar(255)  NOT NULL
        );
        """
        await self.execute(sql, execute=True)
    
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id, location, phone_number):
        sql = "INSERT INTO Users (full_name, username, telegram_id, location, phone_number) VALUES($1, $2, $3, $4, $5) returning *"
        return await self.execute(sql, full_name, username, telegram_id,location , phone_number, fetchrow=True)

    async def get_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)


    async def get_user_by_id(self, user_id):
        sql = "SELECT * FROM Users WHERE telegram_id = $1"
        return await self.execute(sql, user_id, fetchrow=True)


    async def delete_all_users(self):
        sql = "DELETE FROM Users"
        await self.execute(sql, execute=True)
    async def delete_all_products(self):
        sql = "DELETE FROM Products"
        await self.execute(sql, execute=True)

    async def add_product(self, name, price, amount, type, category, image):
        sql = "INSERT INTO Products (name, price, amount, type, category, image) VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql, name, price, amount,type , category, image, fetchrow=True)

    async def get_food_products(self):
        sql = "SELECT * FROM Products WHERE type = 'oziq-ovqat'"
        return await self.execute(sql, fetch=True)

    async def get_distinct_food_categories(self):
        sql = "SELECT DISTINCT category FROM Products WHERE type = 'oziq-ovqat'"
        return await self.execute(sql, fetch=True)
    
    async def get_products_by_category_and_type(self, category, type):
        sql = "SELECT * FROM Products WHERE category = $1 AND type = $2"
        return await self.execute(sql, category, type, fetch=True)

    async def get_product_by_id(self, product_id):
        sql = "SELECT * FROM Products WHERE id = $1"
        return await self.execute(sql, product_id, fetchrow=True)
