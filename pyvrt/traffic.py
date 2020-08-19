from .http import vrt_api_request


def traffic_teaser():
    res = vrt_api_request(
        "traffic",
        "teaser",
        params={"accept": "application/vnd.traffic.vrt.be.teaser_1.0+json"},
    )
    return res


def traffic_jam(km=False):
    traffic_data = traffic_teaser()
    traffic_jam_length = traffic_data["teaser"]["trafficJamLength"]
    if km:
        return {"length": traffic_jam_length / 1000, "unit": "km"}
    else:
        return {"length": traffic_jam_length, "unit": "m"}
