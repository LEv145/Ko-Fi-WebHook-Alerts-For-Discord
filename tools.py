import json
from urllib.parse import unquote # Url Decoder


def get_json_data(config = "config.json"):
	# Open and json reading
	with open(config, "r") as file:
		return json.load(file)

def get_json_decode(data):
	dirty_json = unquote(str(data))
	json_ = json.loads(dirty_json[7:][:-1]) # Trim the excess for Json
	return json_
