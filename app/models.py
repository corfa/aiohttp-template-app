import asyncpg
from dataclasses import dataclass, asdict



@dataclass
class Task:
    id: int
    description: str
    
    @classmethod
    def from_db(cls, row: asyncpg.Record) -> 'Task':
        return cls(id = row['id'], description = row['description'])