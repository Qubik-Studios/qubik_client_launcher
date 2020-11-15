import json
from urllib import request


class account:
    def __init__(self, email, password, clientToken):
        self.server_url = 'https://authserver.mojang.com/'
        self.headers = {'Content-type': 'application/json'}
        self.clientToken = clientToken
        self.email = email
        self._password = password

    def authenticate(self):
        authenticate_url = self.server_url + 'authenticate'

        auth_payload = {
            "agent": {"name": "Minecraft", "version": "1"},
            "username": self.email,
            "password": self._password
        }
        if self.clientToken:
            auth_payload['clientToken'] = self.clientToken

        auth_requ = request.Request(url=authenticate_url,
                                    headers=self.headers,
                                    data=json.dumps(auth_payload).encode())

        auth_resp = json.loads(request.urlopen(auth_requ).read().decode())

        self.accessToken = auth_resp['accessToken']
        self.clientToken = auth_resp['clientToken']
        self.uuid = auth_resp['selectedProfile']['id']
        self.display_name = auth_resp['selectedProfile']['name']
        return True

    def refresh(self, accessToken, clientToken):
        refresh_url = self.server_url + 'refresh'

        refresh_payload = {
            "accessToken": accessToken,
            "clientToken": clientToken
        }
        refresh_requ = request.Request(url=refresh_url,
                                       headers=self.headers,
                                       data=json.dumps(refresh_payload).encode())

        refresh_resp = json.loads(request.urlopen(refresh_requ).read().decode())

        self.accessToken = refresh_resp['accessToken']
        self.clientToken = refresh_resp['clientToken']
        self.uuid = refresh_resp['selectedProfile']['id']
        self.display_name = refresh_resp['selectedProfile']['name']

        return True

    def validate(self, accessToken, clientToken):
        validate_url = self.server_url + 'validate'

        validate_payload = {
            "accessToken": accessToken,
            "clientToken": clientToken
        }

        validate_requ = request.Request(url=validate_url,
                                        headers=self.headers,
                                        data=json.dumps(validate_payload).encode())

        request.urlopen(validate_requ).read().decode()

        return True