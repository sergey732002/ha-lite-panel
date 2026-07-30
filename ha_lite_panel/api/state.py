from aiohttp import web

import cache
import ha
import settings


async def state(request):

    panel_name = request.query.get(
        "panel",
        settings.DEFAULT_PANEL
    )

    panel = ha.load_panel(panel_name)

    result = {}

    for item in panel:

        entity = item.get("entity")

        if not entity:
            continue

        obj = cache.get(entity)

        if obj is None:
            continue

        attributes = obj.get(
            "attributes",
            {}
        )

        result[entity] = {

            "state": obj.get(
                "state",
                ""
            ),

            "unit": attributes.get(
                "unit_of_measurement",
                ""
            )

        }

    return web.json_response(result)