import os
import aiohttp

SUPERVISOR = "http://supervisor/core/api"

TOKEN = os.getenv("SUPERVISOR_TOKEN")


class HomeAssistantError(Exception):
    pass


async def get_states():

    if not TOKEN:
        raise HomeAssistantError(
            "SUPERVISOR_TOKEN not found"
        )

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession(headers=headers) as session:

        async with session.get(
            f"{SUPERVISOR}/states"
        ) as response:

            if response.status != 200:
                text = await response.text()

                raise HomeAssistantError(
                    f"Home Assistant API returned "
                    f"{response.status}: {text}"
                )

            return await response.json()