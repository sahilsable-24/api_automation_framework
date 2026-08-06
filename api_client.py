import requests

class APIClient:

    def __init__(self, base_url,api_key=None):
        self.base_url = base_url
        self.session = requests.session()
        if api_key:
            self.session.headers.update({"x-api-key": api_key})

    def get(self, endpoint, **kwargs):
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint,data=None, **kwargs):
        return self.session.post(f"{self.base_url}{endpoint}", json=data, **kwargs)

    def put(self, endpoint,data=None, **kwargs):
        return self.session.put(f"{self.base_url}{endpoint}", json=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)