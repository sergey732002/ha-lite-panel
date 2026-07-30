import asyncio

import ha

_states = {}
_running = False


async def worker():

    global _running
    global _states

    if _running:
        return

    _running = True

    while True:

        try:

            states = await ha.get_states()

            cache = {}

            for item in states:

                entity_id = item.get("entity_id")

                if entity_id:
                    cache[entity_id] = item

            _states = cache

        except Exception as err:

            print("Cache error:", err)

        await asyncio.sleep(1)


def get(entity_id):

    return _states.get(entity_id)


def get_all():

    return _states