from aiohttp import web

import ha
import settings


async def load_config(request):

    panel = request.query.get(
        "panel",
        settings.DEFAULT_PANEL
    )

    return web.json_response(
        ha.load_panel(panel)
    )


async def save_config(request):

    panel = request.query.get(
        "panel",
        settings.DEFAULT_PANEL
    )

    data = await request.json()

    config = ha.load_panel(panel)

    entity = data["entity"]

    exists = False

    for item in config:

        if item.get("entity") == entity:

            exists = True

            break

    if not exists:

        config.append({

            "entity": entity,

            "title": data["name"],

            "visible": True

        })

        ha.save_panel(
            panel,
            config
        )

    return web.json_response(
        {
            "success": True
        }
    )


async def delete_config(request):

    data = await request.json()

    panel = data.get(
        "panel",
        settings.DEFAULT_PANEL
    )

    entity = data.get("entity")

    config = ha.load_panel(panel)

    result = []

    for item in config:

        if item.get("entity") != entity:

            result.append(item)

    ha.save_panel(
        panel,
        result
    )

    return web.json_response(
        {
            "success": True
        }
    )
