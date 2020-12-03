from flask import Flask, request
from tools import get_json_data, get_json_decode
from webhook import webhook_send


DATA = get_json_data()

KOFI_IP = DATA["kofi_ip"]
PORT    = DATA["port"]
if not(PORT): # Is empty
	raise Exception("Port is empty")	

app = Flask(__name__)

@app.route("/gets", methods = ["POST"])
def receive_update():
	ip = request.remote_addr		

	if KOFI_IP != "":
		print(ip)
		print(KOFI_IP)
		if ip == KOFI_IP: # Checking for ip
			json_ = get_json_decode(request.get_data())
			webhook_send(json_)
	else: # If the parameter is empty
		try:
			json_ = get_json_decode(request.get_data())
			webhook_send(json_)
		except Exception as e:
			print(e)
	return "OK"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=PORT)
