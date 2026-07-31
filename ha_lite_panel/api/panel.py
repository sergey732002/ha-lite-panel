from aiohttp import web

import cache
import ha
import settings


async def panel(request):

    panel_name = request.query.get(
        "panel",
        settings.DEFAULT_PANEL
    )

    config = ha.load_panel(panel_name)

    result = []


    for item in config:

        entity = item.get("entity")


        if not entity:
            continue


        state = cache.get(entity)


        if state is None:
            continue


        attributes = state.get(
            "attributes",
            {}
        )


        domain = entity.split(".")[0]


        data = {

            "entity": entity,

            "title": item.get(
                "title",
                attributes.get(
                    "friendly_name",
                    entity
                )
            ),

            "visible": item.get(
                "visible",
                True
            ),

            "domain": domain,

            "state": state.get(
                "state",
                ""
            ),

            "unit": attributes.get(
                "unit_of_measurement",
                ""
            ),

            "icon": attributes.get(
                "icon",
                ""
            )

        }


        # -------- MEDIA PLAYER --------

        if domain == "media_player":

            data["volume"] = attributes.get(
                "volume_level",
                0
            )


            data["media_title"] = attributes.get(
                "media_title",
                ""
            )


            data["media_artist"] = attributes.get(
                "media_artist",
                ""
            )


        result.append(data)


    return web.json_response(result)
