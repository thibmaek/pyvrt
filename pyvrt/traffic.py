from .http import vrtnws_api_request


def traffic_teaser():
    res = vrtnws_api_request("traffic", "teaser")
    return res


def traffic_jam(km=False):
    traffic_data = traffic_teaser()

    if traffic_data and traffic_data.get("teaser"):
        traffic_jam_length = traffic_data["teaser"]["trafficJamLength"]
        if km:
            return {"length": traffic_jam_length / 1000, "unit": "km"}
        else:
            return {"length": traffic_jam_length, "unit": "m"}
    else:
        return {}
