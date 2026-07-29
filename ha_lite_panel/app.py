from aiohttp import web

import api
import panel


app = web.Application()

app.router.add_get("/", panel.index)
app.router.add_get("/api/states", api.states)

app.router.add_static("/static/", "/static")

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8099)