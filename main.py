import requests

api = 'https://discordapp.com/api/v9/invites/'#code invite: eU2mYfJ7JF ;D

headrs = {
    "authorization" : ''#token
}

while True: 
    requests.post(api, headers=headrs)
