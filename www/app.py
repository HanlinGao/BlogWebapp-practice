import time
import json
import os
from aiohttp import web
from datetime import datetime
import asyncio
import logging

logging.basicConfig(level=logging.INFO)


async def index(request):
    return web.Response(body=b'<h1>Hello</h1>', content_type='text/html')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    logging.info('Server started at 127.0.0.1...')
    web.run_app(app, host='127.0.0.1', port=8080)


init()


