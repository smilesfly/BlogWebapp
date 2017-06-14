#!usr/bin/env python3
# -*- coding: utf-8 -*-
__author__="Even"
#Web App骨架
import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

#制作响应函数
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

async def init(loop):  #Web app服务器初始化
    app = web.Application(loop=loop) # async 替代 @asyncio.coroutine装饰器,代表这个是要异步运行的函数
    app.router.add_route('GET', '/', index) #把响应函数添加到响应函数集合
    srv =  await  loop.create_server(app.make_handler(), '127.0.0.1', 9000)   #await 代替yield from ,表示要放入asyncio.get_event_loop中进行的异步操作
    logging.info('server started at http://127.0.0.1:9000...')  #创建服务器(连接网址、端口，绑定handler)
    return srv

loop = asyncio.get_event_loop()   #创建asyncio event loop  创建事件
loop.run_until_complete(init(loop))  #用asyncio event loop 来异步运行init()  运行
loop.run_forever() #服务器不关闭