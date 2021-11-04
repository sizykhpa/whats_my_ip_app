from aiohttp import web

routes = web.RouteTableDef()
@routes.get('/')
async def hello(request):
    ip_address = request.headers['X-Real-IP']

    return web.Response(text=f'{ip_address}\n', content_type='text/html')


app = web.Application()
app.add_routes(routes)