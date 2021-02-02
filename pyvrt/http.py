import requests

BASE_URL_VRT_SERVICES = "https://services.vrt.be/{}/{}"
BASE_URL_VRTNWS_API = "https://vrtnws-api.vrt.be/{}/{}"


def vrtnws_api_request(service, path, params=None):
    """Sends a request to the VRTNWS API endpoint"""
    url = BASE_URL_VRTNWS_API.format(service, path)

    try:
        res = requests.get(url, params)
        try:
            return res.json()
        except ValueError:
            return None
    except requests.RequestException as ex:
        print("VRTNWS API request '{}' failed:".format(url), ex)
        return None


def vrt_services_request(service, path, params=None):
    """Sends a request to the VRT Services API"""
    url = BASE_URL_VRT_SERVICES.format(service, path)

    try:
        res = requests.get(url, params)
        try:
            return res.json()
        except ValueError:
            return None

    except requests.RequestException as ex:
        print("VRT Services request '{}' failed:".format(url), ex)
        return None
