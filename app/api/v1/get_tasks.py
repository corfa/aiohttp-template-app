from aiohttp import web

from storage import get_tasks
from context import AppContext
import models

async def handle(request: web.Request, ctx: AppContext) -> web.Response:
    tasks = await get_tasks(context=ctx)

    return web.json_response({"tasks": [
        to_response(task) for task in tasks
        ]})

def to_response(task: models.Task) -> dict:
    return {
        'id':task.id,
        'description': task.description
    }