from .http import vrt_api_request


def __get_zone_from_list(items_list, zone):
    try:
        res = filter(lambda item: item["location"].lower() == zone.lower(), items_list)
        return res
    except (KeyError, StopIteration) as ex:
        raise ValueError("Could not find zone in list", ex, items_list)


def summary(region="BE"):
    if region != "BE":
        raise ValueError("Only region=BE is supported for retrieving summary")

    res = vrt_api_request(
        "weather",
        "weathertalks/belgie_huidig",
        params={"accept": "application/vnd.weather.vrt.be.weathertalks_1.0+json"},
    )

    if res:
        return res["weathertalk"]
    else:
        return None


def current(region="BE", zone=None):
    if region == "BE":
        res = vrt_api_request(
            "weather",
            "observations/belgische_streken",
            params={"accept": "application/vnd.weather.vrt.be.observations_1.0+json"},
        )

    if zone:
        zone_res = next(__get_zone_from_list(res["observations"], zone))
        zone_res["date"] = res["date"]
        return zone_res

    return res

    if region == "EU":
        res = vrt_api_request(
            "weather",
            "observations/europese_steden",
            params={"accept": "application/vnd.weather.vrt.be.observations_1.0+json"},
        )

    if zone:
        zone_res = next(__get_zone_from_list(res["observations"], zone))
        zone_res["date"] = res["date"]
        return zone_res
    else:
        return res


def forecast(region="BE", zone=None):
    if region == "BE":
        res = vrt_api_request(
            "weather",
            "forecasts/belgische_streken",
            params={"accept": "application/vnd.weather.vrt.be.forecasts_1.0+json"},
        )

        if zone:
            return {
                "date": res["date"],
                "forecasts": list(__get_zone_from_list(res["forecasts"], zone)),
            }
        else:
            return res

    if region == "EU":
        res = vrt_api_request(
            "weather",
            "forecasts/europese_steden",
            params={"accept": "application/vnd.weather.vrt.be.forecasts_1.0+json"},
        )

        if zone:
            return {
                "date": res["date"],
                "forecasts": list(__get_zone_from_list(res["forecasts"], zone)),
            }
        else:
            return res
