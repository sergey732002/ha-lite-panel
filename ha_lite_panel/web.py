from aiohttp import web


async def index(request):

    return web.FileResponse(
        "/templates/index.html"
    )