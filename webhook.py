import discord
from discord import Webhook, RequestsWebhookAdapter
from tools import get_json_data, random_color
from tools import get_json_decode
from datetime import datetime

DATA = get_json_data()

WEBHOOK_URL = DATA["webhook_url"]

if not(WEBHOOK_URL):
    raise ValueError("Webhook url is empty")

# Test Data
"""
{'message_id': 'da75b014-117c-481c-a64f-e6086e407e26', 
 'timestamp': '2020-12-03T12:36:20.5745667Z', 
 'type': 'Donation', 
 'is_public': True, 
 'from_name': 'John+Smith', 
 'message': 'Good+luck+with+the+integration!', 
 'amount': '3.00', 
 'url': 'https://ko-fi.com', 
 'email': None, 'currency': None, 
 'is_subscription_payment': False, 
 'is_first_subscription_payment': False, 
 'kofi_transaction_id': '1234-1234-1234-1234'}
"""

def webhook_send(json_):
	# If public
	if not(json_['is_public']):
		return

	webhook = Webhook.from_url(WEBHOOK_URL, adapter = RequestsWebhookAdapter())

	# Embed
	embed = discord.Embed(title = "Donate!",
                          timestamp = datetime.utcnow(),
                          color = random_color())

	embed.add_embed_field(value = f"{json_['from_name'].replace('+', ' ')}",   name = "Donater", inline = False)
	embed.add_embed_field(value = f"{json_['message'].replace('+', ' ')}",     name = "Message", inline = False)
	embed.add_embed_field(value = f"{json_['amount']}$",                       name = "Amount of money", inline = False)
	#embed.add_embed_field(value = f"{json_['email']}",                         name = "Email", inline = False)
	#embed.add_embed_field(value = f"{json_['kofi_transaction_id']}",           name = "Transaction id", inline = False)
	#embed.add_embed_field(value = f"{json_['is_subscription_payment']}",       name = "Subscription payment", inline = False)
	#embed.add_embed_field(value = f"{json_['is_first_subscription_payment']}", name = "First subscription payment", inline = False)

	#embed.set_footer(text = f"{json_['timestamp'][:10]} • {json_['timestamp'][11:19]}")

	webhook.send(embed = embed)
