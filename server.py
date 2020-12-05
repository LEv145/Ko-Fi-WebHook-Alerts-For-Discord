from aiohttp import web
from tools import get_json_data, get_json_decode
from webhook import webhook_send

DATA = get_json_data()

KOFI_IP = DATA["kofi_ip"]
PORT    = DATA["port"]
if not(PORT): # Is empty
	raise Exception("Port is empty")	

routes = web.RouteTableDef() # routes

@routes.post('/gets')
async def receive_update(request):
	ip = request.remote	
	print(ip)	
	
	data = await request.read()

	if KOFI_IP != "":
		if ip == KOFI_IP: # Checking for ip
			json_ = get_json_decode(data)
			webhook_send(json_)
	else: # If the parameter is empty
		try:
			json_ = get_json_decode(data)
			webhook_send(json_)
		except Exception as e:
			print(e)
	return web.Response(text='OK')

# Init Server
async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app


web.run_app(init_app(), host="0.0.0.0", port=PORT)
