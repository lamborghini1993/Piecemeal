import logging
import asyncio
import os
import json
import time

from aiohttp import web

from datetime import datetime

logging.basicConfig(level=logging.INFO)


async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', "/", index)
    srv = await loop.create_server(app.make_handler(), "127.0.0.1", 9000)
    # srv = await loop.create_server(web.AppRunner(app), "127.0.0.1", 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
