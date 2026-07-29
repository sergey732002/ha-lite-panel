from aiohttp import web
import ha


async def states(request):
    try:
        data = await ha.get_states()
        return web.json_response(data)
    except Exception as e:
        return web.json_response(
            {
                "success": False,
                "error": str(e)
            },
            status=500
        )