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


async def move_up(request):

    data = await request.json()

    panel = data.get(
        "panel",
        settings.DEFAULT_PANEL
    )

    entity = data.get("entity")

    config = ha.load_panel(panel)

    for i in range(1, len(config)):

        if config[i]["entity"] == entity:

            config[i - 1], config[i] = (
                config[i],
                config[i - 1]
            )

            break

    ha.save_panel(
        panel,
        config
    )

    return web.json_response(
        {
            "success": True
        }
    )


async def move_down(request):

    data = await request.json()

    panel = data.get(
        "panel",
        settings.DEFAULT_PANEL
    )

    entity = data.get("entity")

    config = ha.load_panel(panel)

    for i in range(
        len(config) - 1
    ):

        if config[i]["entity"] == entity:

            config[i], config[i + 1] = (
                config[i + 1],
                config[i]
            )

            break

    ha.save_panel(
        panel,
        config
    )

    return web.json_response(
        {
            "success": True
        }
    )
