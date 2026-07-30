from aiohttp import web

import ha


SERVICE_MAP = {
    "light": {
        "toggle": "toggle",
        "on": "turn_on",
        "off": "turn_off"
    },

    "switch": {
        "toggle": "toggle",
        "on": "turn_on",
        "off": "turn_off"
    },

    "fan": {
        "toggle": "toggle",
        "on": "turn_on",
        "off": "turn_off"
    },

    "input_boolean": {
        "toggle": "toggle",
        "on": "turn_on",
        "off": "turn_off"
    },

    "cover": {
        "open": "open_cover",
        "close": "close_cover",
        "stop": "stop_cover"
    },

    "scene": {
        "activate": "turn_on"
    },

    "script": {
        "run": "turn_on"
    }
}


async def service(request):

    try:
        data = await request.json()

    except Exception:

        return web.json_response(
            {
                "success": False
            },
            status=400
        )

    entity = data.get("entity")
    action = data.get("action")

    if not entity or not action:

        return web.json_response(
            {
                "success": False
            },
            status=400
        )

    domain = entity.split(".")[0]

    if domain not in SERVICE_MAP:

        return web.json_response(
            {
                "success": False
            },
            status=400
        )

    if action not in SERVICE_MAP[domain]:

        return web.json_response(
            {
                "success": False
            },
            status=400
        )

    result = await ha.call_service(

        domain,

        SERVICE_MAP[domain][action],

        entity

    )

    return web.json_response(

        {
            "success": bool(result)
        }

    )