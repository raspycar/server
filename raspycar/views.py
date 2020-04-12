from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


def index(request):
    return templates.TemplateResponse("index.html", {"request": request})


async def ws(websocket):
    await websocket.accept()
    await websocket.send_text("Hello")
    await websocket.close()
