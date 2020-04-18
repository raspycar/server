from starlette.templating import Jinja2Templates

from . import settings

templates = Jinja2Templates(directory="templates")


def index(request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "video_url": settings.VIDEO_URL}
    )


async def ws(websocket):
    await websocket.accept()
    await websocket.send_text("Hello")
    await websocket.close()
