import requests

data = {
    'usage_user_id': 1431,
    'usage_channel_id': 24
}

data = {
    'channel_id': 1
}

url = "http://127.0.0.1:8000/api/get_channels/"

res = requests.get(url)

r = res.json()

for i in r:
    print(i['fields']['channel_id'])