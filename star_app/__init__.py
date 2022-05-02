from starlette.applications import Starlette
from . import routes


app = Starlette(debug=True, routes=routes.routes)