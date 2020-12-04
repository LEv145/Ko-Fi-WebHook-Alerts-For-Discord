import json
from discord import Color
from urllib.parse import unquote # Url Decoder
from random import randint

def random_color():
    return Color.from_rgb(randint(1, 255), randint(1, 255), randint(1, 255))

def get_json_data(config = "config.json") -> None:
	# Open and json reading
	with open(config, "r") as file:
		return json.load(file)

def get_json_decode(data) -> str:
	dirty_json = unquote(str(data))
	json_ = json.loads(dirty_json[7:][:-1]) # Trim the excess for Json
	return json_
