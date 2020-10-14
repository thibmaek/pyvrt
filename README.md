# pyvrt

🐍 Python library to interact with VRT public APIs (weather, traffic…)

## Usage

```python
import pyvrt.traffic as traffic
import pyvrt.weather as weather

weather.summary()
weather.forecast(region='BE', zone='kust')

traffic.traffic_jam(km=True)
```

## Development

```shell
$ make install
$ make build
```
