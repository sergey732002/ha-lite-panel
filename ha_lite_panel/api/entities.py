from aiohttp import web

import cache
import ha
import settings


async def entities(request):

    panel = request.query.get(
        "panel",
        settings.DEFAULT_PANEL
    )

    config = ha.load_panel(panel)

    selected = []

    for item in config:

        entity = item.get("entity")

        if entity:

            selected.append(entity)

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

            "domain": entity_id.split(".")[0],

            "added": entity_id in selected

        })

    return web.json_response(
        result
    )
