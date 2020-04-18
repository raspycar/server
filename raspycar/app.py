from starlette.applications import Starlette
from starlette.routing import Mount, Route, WebSocketRoute
from starlette.staticfiles import StaticFiles

from raspycar.views import index, ws

routes = (
    Route("/", index),
    WebSocketRoute("/ws", ws),
    Mount("/static", StaticFiles(directory="static")),
)


app = Starlette(debug=True, routes=routes)
