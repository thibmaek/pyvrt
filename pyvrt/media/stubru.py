from ..http import vrt_api_request
from .const import CHANNEL_CODE_STUBRU


def __get_image_url(image_urls):
    try:
        res = filter(lambda item: item["destinations"] == "radioplus", image_urls)
        return res
    except (KeyError, StopIteration) as ex:
        raise ValueError("Could not find a suitable image", ex, image_urls)


def get_onair():
    onairs = vrt_api_request(
        "epg",
        "onair",
        params={
            "accept": "application/vnd.epg.vrt.be.onairs_1.2+json",
            "channel_code": str(CHANNEL_CODE_STUBRU),
        },
    )
    if onairs and onairs.get("onairs"):
        return onairs["onairs"][0]
    else:
        return {}


def previous():
    onair = get_onair()

    if onair.get("previous"):
        item = onair["previous"]
        imageItem = next(__get_image_url(item["imageurls"]))
        return {
            "title": item["title"],
            "description": item["description"],
            "startTime": item["startTime"],
            "endTime": item["endTime"],
            "image": imageItem["url"] if imageItem else None,
        }
    else:
        return {}


def next_up():
    onair = get_onair()

    if onair.get("next"):
        item = onair["next"]
        imageItem = next(__get_image_url(item["imageurls"]))
        return {
            "title": item["title"],
            "description": item["description"],
            "startTime": item["startTime"],
            "endTime": item["endTime"],
            "image": imageItem["url"] if imageItem else None,
        }
    else:
        return {}


def current():
    onair = get_onair()

    if onair.get("now"):
        item = onair["now"]
        imageItem = next(__get_image_url(item["imageurls"]))
        return {
            "title": item["title"],
            "description": item["description"],
            "startTime": item["startTime"],
            "endTime": item["endTime"],
            "image": imageItem["url"] if imageItem else None,
        }
    else:
        return {}
