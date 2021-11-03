from aiohttp import web

routes = web.RouteTableDef()
@routes.get('/')
async def hello(request):
    ip_address = request.headers['X-Real-IP']

    return web.Response(text=ip_address)

app = web.Application()
app.add_routes(routes)
