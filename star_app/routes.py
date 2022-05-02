from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from . import views, settings





routes = [
    Mount("/static", app=StaticFiles(directory=settings.BASE_DIR / "static"), name="static"),
    Route("/", endpoint=views.homepage, name='home'),
    ]