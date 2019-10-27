


import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=r'<h1>Hello, world!</h1>', headers={'content-type':'text/html'})


async def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/', index)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    await site.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()