__version__ = "0.1.0"

from starlette.applications import Starlette
from starlette.routing import Mount, Route, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")


def index(request):
    return templates.TemplateResponse("index.html", {"request": request})


async def ws(websocket):
    await websocket.accept()
    await websocket.send_text("Hello")
    await websocket.close()


routes = (
    Route("/", index),
    WebSocketRoute("/ws", ws),
    Mount("/static", StaticFiles(directory="static")),
)


app = Starlette(debug=True, routes=routes)
