#### KoFI-Python-Webhook-API-Server
Server for KoFI Webhook API

![Иллюстрация к проекту](https://media.discordapp.net/attachments/675064990893604894/784100468560232488/unknown.png?width=263&height=361)


# How to Use

* Edit config.json

Config examples:
```json
{
	"webhook_url": "https://discord.com/api/webhooks/777622373691555879/3dIG3cH5dE7vB-J000t2pSyjRXxCBL_kibP_CunUeeH-K3rjr3GykB5Oz32vzaUnvP4N",
	"port": 8080,
	"kofi_ip": "104.45.233.233"
}
```
```json
{
	"webhook_url": "https://discord.com/api/webhooks/777622373691555879/3dIG3cH5dE7vB-J000t2pSyjRXxCBL_kibP_CunUeeH-K3rjr3GykB5Oz32vzaUnvP4N",
	"port": 7000,
	"kofi_ip": ""
}
```

* Install requirements(cmd/bash):
```cmd
python3 -m pip install -r requirements.txt
```

* Run server.py(cmd/bash):
```cmd
python3 server.py
```
(Download python here: https://www.python.org/)


* Go to https://ko-fi.com/manage/webhooks and enter your server IP/domain with /gets.

Examples:
```
http://212.323.232.321:8080/gets
```
```
http://212.323.232.211:7000/gets
```
* Press **Update** Button end have enjoy!

# Donate:3
https://money.yandex.ru/to/410015858804944/0
