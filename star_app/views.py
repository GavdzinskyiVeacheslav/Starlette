from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
from .import settings

templates = Jinja2Templates(directory=settings.BASE_DIR / 'templates')

async def homepage(request):
    template = 'homepage.html'
    context = {
        'request': request
    }
    return templates.TemplateResponse(template, context)