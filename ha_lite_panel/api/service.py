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
    },


    "media_player": {

        "play": "media_play",

        "pause": "media_pause",

        "next": "media_next_track"

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



    entity = data.get(
        "entity"
    )

    action = data.get(
        "action"
    )



    if not entity or not action:

        return web.json_response(

            {
                "success": False
            },

            status=400

        )



    domain = entity.split(".")[0]



    # -------------------------
    # MEDIA PLAYER VOLUME
    # -------------------------

    if (

        domain == "media_player"

        and action in (

            "volume_up",

            "volume_down"

        )

    ):


        current = data.get(
            "volume",
            0.5
        )


        try:

            current = float(
                current
            )

        except Exception:

            current = 0.5



        step = 0.05



        if action == "volume_up":

            current += step


        else:

            current -= step



        if current < 0:

            current = 0



        if current > 1:

            current = 1



        result = await ha.call_service(

            domain,

            "volume_set",

            entity,

            {

                "volume_level": current

            }

        )



        return web.json_response(

            {
                "success": bool(result)
            }

        )





    # -------------------------
    # MEDIA PLAYER OTHER
    # -------------------------

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
