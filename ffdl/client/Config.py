

class Config:
    def __init__(self, api_endpoint=None, api_version='v1', version='2017-02-13', user=None, password=None, user_info=None):
        self._api_endpoint = api_endpoint
        self._api_version = api_version
        self._version = version
        self._user = user
        self._password = password
        self._user_info = user_info

    @property
    def api_endpoint(self):
        return self._api_endpoint

    @property
    def api_version(self):
        return self._api_version

    @property
    def version(self):
        return self._version

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def user_info(self):
        return self._user_info

    def is_valid(self):
        if not self._api_endpoint:
            raise ValueError('FfDL API endpoint is required')

        if not self._user:
            raise ValueError('FfDL user is required')

        if not self._user_info:
            raise ValueError('FfDL user info required')

        return True
