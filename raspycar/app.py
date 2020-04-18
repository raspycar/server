from starlette.applications import Starlette
from starlette.routing import Mount, Route, WebSocketRoute
from starlette.staticfiles import StaticFiles

from . import controls
from .views import index, ws

routes = (
    Route("/", index),
    WebSocketRoute("/ws", ws),
    Mount("/static", StaticFiles(directory="static")),
)


async def stop_car():
    controls.stop()


app = Starlette(debug=True, routes=routes, on_shutdown=[stop_car])
