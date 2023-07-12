import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

class AppContext:
    def __init__(self):
        self.db_url = os.getenv('URL_DB','') 
        self.db = None

    async def on_startup(self, app = None):
        self.db = await asyncpg.create_pool(self.db_url)
    
    async def on_shutdown(self, app = None):
        if self.db:
            await self.db.close()