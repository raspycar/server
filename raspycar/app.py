import logging

from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from . import controls, settings

logger = logging.getLogger(__file__)
routes = (Mount("/static", StaticFiles(directory="static")),)
templates = Jinja2Templates(directory="templates")


async def emergency_stop():
    """Stop the car on disconnection or app shutdown"""
    controls.stop()


# Web app
app = Starlette(debug=True, routes=routes, on_shutdown=[emergency_stop])

# Routes
@app.route("/")
def index(request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "video_url": settings.VIDEO_URL}
    )


@app.websocket_route("/ws")
class ControlWebsocketEndpoint(WebSocketEndpoint):
    async def on_connect(self, websocket):
        await websocket.accept()

    async def on_disconnect(self, websocket, close_code):
        await emergency_stop()
        await websocket.close()

    async def on_receive(self, websocket, data):
        logger.info('Received control "%s"', data)
        callback = getattr(controls, data, None)
        if callback is not None:
            callback()
        else:
            logger.error("Control not found!")
