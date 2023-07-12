import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

class AppContext:
    """Represents the application context for database connection.

    This class manages the database connection and provides startup and shutdown handlers
    for setting up and closing the database connection pool.

    Attributes:
        db_url (str): The URL of the database.
        db: The database connection pool.

    Methods:
        on_startup: A coroutine that sets up the database connection pool on application startup.
        on_shutdown: A coroutine that closes the database connection pool on application shutdown.
    """
    def __init__(self):
        self.db_url = os.getenv('URL_DB', '')
        self.db = None

    async def on_startup(self, app=None):
        
        self.db = await asyncpg.create_pool(self.db_url)

    async def on_shutdown(self, app=None):
       
        if self.db:
            await self.db.close()
