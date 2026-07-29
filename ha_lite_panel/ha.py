import aiohttp
import os

SUPERVISOR = "http://supervisor/core/api"
TOKEN = os.environ.get("SUPERVISOR_TOKEN")


async def get_states():

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession(headers=headers) as session:

        async with session.get(
            SUPERVISOR + "/states"
        ) as resp:

            return await resp.json()