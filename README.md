# pyvrt

🐍 Python library to interact with VRT public APIs (weather, traffic…)

## Usage

```python
from pyvrt import traffic, weather

weather.summary()
weather.forecast(region='BE', zone='kust')

traffic.trafficJam(km=True)
```

## Development

```shell
$ python setup.py install
```
