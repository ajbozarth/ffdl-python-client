import requests

from ffdl.client import Config
from requests.auth import HTTPBasicAuth


class FfDLClient:
    def __init__(self, config:Config):
        """
        :param config: FfDL connection configuration
        """
        self.config = config

    def get(self, url):
        """
        Submit a get request to a FfDL server
        :param url: the api url path
        :return: a json payload with the api result
        """
        # validate that proper configuration has been provided
        self.config.is_valid()

        # accomodate provided strings starting with '/'
        if url.startswith('/'):
            url = url[1:]

        endpoint = self._create_ffdl_endpoint(url)

        headers = {'accept': 'application/json',
                   'X-Watson-Userinfo': self.config.user_info}

        try:
            response = requests.get(endpoint,
                                  auth=HTTPBasicAuth(self.config.user, self.config.password),
                                  headers=headers)

            if not response:
                raise RuntimeError("Error submitting job to FfDL")

            return response

        except requests.exceptions.Timeout:
            print("FfDL Job Submission Request Timed Out....")
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects were detected during job submission")
        except requests.exceptions.ConnectionError:
            print("Connection Error: Could not connect to {}".format(endpoint))
        except requests.exceptions.HTTPError as http_err:
            print("HTTP Error - {} ".format(http_err))
        except requests.exceptions.RequestException as err:
            print(err)

    def post(self, url, **file_paths):
        """
        Submit a post request to a FfDL server
        :param url: the api url path
        :param file_paths: files to submit with the post request
        :return: a json payload with the api result
        """
        # validate that proper configuration has been provided
        self.config.is_valid()

        # accomodate provided strings starting with '/'
        if url.startswith('/'):
            url = url[1:]

        endpoint = self._create_ffdl_endpoint(url)

        headers = {'accept': 'application/json',
                   'X-Watson-Userinfo': self.config.user_info}

        files = {}
        for name, path in file_paths.items():
            files[name] = open(file_paths[name], 'rb')

        try:
            result = requests.post(endpoint,
                                   auth=HTTPBasicAuth(self.config.user, self.config.password),
                                   headers=headers,
                                   files=files)

            return result.json()

        except requests.exceptions.Timeout:
            print("FfDL Job Submission Request Timed Out....")
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects were detected during job submission")
        except requests.exceptions.ConnectionError:
            print("Connection Error: Could not connect to {}".format(endpoint))
        except requests.exceptions.HTTPError as http_err:
            print("HTTP Error - {} ".format(http_err))
        except requests.exceptions.RequestException as err:
            print(err)

        finally:
            for name, file in files.items():
                file.close()

    def _create_ffdl_endpoint(self, url):
        """
        Utility method to create the FfDL api url based on FfDL
        server endpoint, api version and model version
        :param url:
        :return:
        """
        return "{}/{}/{}?version={}".format(self.config.api_endpoint, self.config.api_version, url, self.config.version)
