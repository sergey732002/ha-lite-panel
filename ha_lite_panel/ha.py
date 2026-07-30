import aiohttp
import json
import os

import settings

SUPERVISOR = "http://supervisor/core/api"
TOKEN = os.environ.get("SUPERVISOR_TOKEN")


async def request(url, method="GET", data=None):

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession(
        headers=headers
    ) as session:

        if method == "GET":

            async with session.get(url) as resp:

                return await resp.json()

        if method == "POST":

            async with session.post(
                url,
                json=data
            ) as resp:

                if resp.status in (200, 201):
                    return True

                try:
                    return await resp.json()
                except Exception:
                    return False

    return False


async def get_states():

    return await request(
        SUPERVISOR + "/states"
    )


async def call_service(
    domain,
    service,
    entity_id
):

    return await request(
        f"{SUPERVISOR}/services/{domain}/{service}",
        method="POST",
        data={
            "entity_id": entity_id
        }
    )


def panel_path(name):

    return os.path.join(
        settings.PANELS_DIR,
        name + ".json"
    )


def load_panel(name):

    path = panel_path(name)

    if not os.path.exists(path):
        return []

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return []


def save_panel(name, data):

    path = panel_path(name)

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def get_panel_entities(name):

    panel = load_panel(name)

    result = []

    for item in panel:

        if isinstance(item, str):

            result.append(item)

            continue

        if isinstance(item, dict):

            entity = item.get("entity")

            if entity:

                result.append(entity)

    return result