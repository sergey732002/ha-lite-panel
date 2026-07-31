from aiohttp import web

import cache
import settings


async def header(request):

    states = cache.get_all()

    temperature = None

    entity = settings.WEATHER_ENTITY

    if entity in states:

        data = states[entity]

        attributes = data.get(
            "attributes",
            {}
        )

        temperature = attributes.get(
            "temperature"
        )

    return web.json_response({

        "temperature": temperature

    })
