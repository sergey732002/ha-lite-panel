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

    config.append({

        "entity": data["entity"],

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