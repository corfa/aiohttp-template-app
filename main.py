from app import routes
from aiohttp import web
from app.context import AppContext

import asyncio

async def create_app():
    ctx = AppContext()
    app = web.Application()
    app.on_startup.append(ctx.on_startup)
    app.on_shutdown.append(ctx.on_shutdown)
    routes.setup_routes(app, ctx)
    return app

def main():
    app = asyncio.get_event_loop().run_until_complete(create_app())
    web.run_app(app)

if __name__ == '__main__':
    main()
