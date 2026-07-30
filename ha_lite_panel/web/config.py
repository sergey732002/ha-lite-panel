from aiohttp import web


async def config_page(request):

    return web.FileResponse(
        "/templates/config.html"
    )