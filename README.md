# How-to-send-a-message-to-a-specific-channel-
How to send a message to a specific channel 

```python
#!/usr/bin/python3

import requests

# message
payload = {
    'content': 'hello world'
}

header = {
    'authorization': 'TOKEN'
}

# channel redlive13
r = requests.post(
    'https://discord.com/api/v8/channels/816350000862461982/messages', data=payload, headers=header)
```
