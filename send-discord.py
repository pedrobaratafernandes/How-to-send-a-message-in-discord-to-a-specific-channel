#!/usr/bin/python3

import requests

payload = {
    'content': 'hello world'
}

header = {
    'authorization': 'ODE2NDY3MDg2NDE4MTE2NjM5.YFN43Q.6k4H4YN4nE6EsQ4JgOMxYs09eWA'
}

r = requests.post(
    'https://discord.com/api/v8/channels/816350000862461982/messages', data=payload, headers=header)
