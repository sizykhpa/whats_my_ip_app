from aiohttp import web

routes = web.RouteTableDef()
@routes.get('/')
async def hello(request):
    ip_address = request.headers['X-Real-IP']
    html_response = f'<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{ip_address}</pre></body></html>'

    return web.Response(text=html_response, content_type='text/html')

app = web.Application()
app.add_routes(routes)
