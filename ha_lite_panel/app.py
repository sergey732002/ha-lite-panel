import asyncio
from aiohttp import web

async def index(request):
    return web.Response(text="""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>HA Lite Panel</title>
<link rel="stylesheet" href="/static/style.css">
</head>
<body>
<div class="box">
<h1>HA Lite Panel</h1>
<p>v0.1.0 работает</p>
<p>AIOHTTP OK</p>
</div>
<script src="/static/app.js"></script>
</body>
</html>
""", content_type="text/html")

async def websocket(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    await ws.send_str("WebSocket connected")
    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            await ws.send_str(msg.data)
    return ws

async def main():
    app = web.Application()
    app.router.add_get("/", index)
    app.router.add_get("/ws", websocket)
    app.router.add_static("/static/", "/static/")
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8099)
    await site.start()
    while True:
        await asyncio.sleep(3600)

asyncio.run(main())
