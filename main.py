from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text=request.headers['X-Real-IP'])

app = web.Application()
app.add_routes(routes)
