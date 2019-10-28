


import logging
logging.basicConfig(level=logging.INFO)
import www.orm
from www.models import User, Blog, Comment

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


# 创建响应函数，当访问路由路径\的时候会调用该函数
def index(request):
    return web.Response(body=r'<h1>Hello, world!</h1>', headers={'content-type':'text/html'})


# 初始化设置
# 设置路由将网址与调用的函数关联起来
# 并设置响应路径
async def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/', index)
    runner = web.AppRunner(app)
    # 耗时的异步操作需要等待
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    # 同是耗时任务，需要等待
    await site.start()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

async def test(loop):
    await www.orm.create_pool(loop=loop, user='www-data', password='www-data',
                              db='awesome')
    u = User(name = "Test1", email = "ew@watson.com", passwd = '1234567890',
             image = "about:blank")
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.run_forever()