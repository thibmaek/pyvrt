# pyvrt

🐍 Python library to interact with VRT public APIs (weather, traffic…)

## Usage

```python
from pyvrt.traffic import traffic
from pyvrt.weather import weather

weather.summary()
weather.forecast(region='BE', zone='kust')

traffic.trafficJam(km=True)
```

## Development

```shell
$ make install
$ make build
```
