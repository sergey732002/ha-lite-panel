from aiohttp import web

import cache


async def entities(request):

    states = cache.get_all()

    result = []

    for entity_id in sorted(states):

        item = states[entity_id]

        attributes = item.get(
            "attributes",
            {}
        )

        result.append({

            "entity": entity_id,

            "name": attributes.get(
                "friendly_name",
                entity_id
            ),

            "domain": entity_id.split(".")[0]

        })

    return web.json_response(result)