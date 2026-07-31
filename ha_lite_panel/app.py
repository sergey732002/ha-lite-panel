from aiohttp import web

import asyncio
import cache

from api.entities import entities
from api.panel import panel
from api.state import state
from api.service import service

from api.config import (
    load_config,
    save_config,
    delete_config,
    move_up,
    move_down
)

from web.index import index
from web.config import config_page

import settings


app = web.Application()


# ---------- WEB ----------

app.router.add_get(
    "/",
    index
)

app.router.add_get(
    "/config",
    config_page
)


# ---------- API ----------

app.router.add_get(
    "/api/entities",
    entities
)

app.router.add_get(
    "/api/panel",
    panel
)

app.router.add_get(
    "/api/state",
    state
)

app.router.add_post(
    "/api/service",
    service
)

app.router.add_get(
    "/api/config",
    load_config
)

app.router.add_post(
    "/api/config",
    save_config
)

app.router.add_post(
    "/api/delete",
    delete_config
)

app.router.add_post(
    "/api/move_up",
    move_up
)

app.router.add_post(
    "/api/move_down",
    move_down
)


# ---------- STATIC ----------

app.router.add_static(
    "/static/",
    settings.STATIC_DIR
)


# ---------- CACHE ----------

async def on_startup(application):

    asyncio.create_task(
        cache.worker()
    )


app.on_startup.append(
    on_startup
)


# ---------- START ----------

web.run_app(
    app,
    host="0.0.0.0",
    port=8099
)
