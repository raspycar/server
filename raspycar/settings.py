from starlette.config import Config

config = Config(".env")
VIDEO_URL = config("VIDEO_URL", default="")
