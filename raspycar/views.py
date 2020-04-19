import logging

from starlette.templating import Jinja2Templates

from . import controls, settings

logger = logging.getLogger(__file__)
templates = Jinja2Templates(directory="templates")


def index(request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "video_url": settings.VIDEO_URL}
    )


async def ws(websocket):
    await websocket.accept()
    while True:
        text = await websocket.receive_text()
        logger.info('Received control "%s"', text)
        callback = getattr(controls, text[0], None)
        if callback is not None:
            callback()
    await websocket.close()
    controls.stop()
