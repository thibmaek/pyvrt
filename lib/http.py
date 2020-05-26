import requests

BASE_URL = "https://services.vrt.be/{}/{}"


def vrt_api_request(service, path, params=None):
    url = BASE_URL.format(service, path)

    try:
        res = requests.get(url, params)
        try:
            json_res = res.json()
            return json_res
        except ValueError:
            return None

    except requests.RequestException as ex:
        print("Failed to do VRT API request:", ex)
        return None
