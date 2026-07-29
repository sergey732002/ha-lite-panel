from aiohttp import web
import ha


async def states(request):

    data = await ha.get_states()

    return web.json_response(data)