[![Supported Python versions](https://img.shields.io/pypi/pyversions/coffeepy.svg?style=flat)](https://pypi.python.org/pypi/coffeepy/) [![PyPI Version](https://img.shields.io/pypi/v/coffeepy.svg)](https://pypi.python.org/pypi/coffeepy)
# Coffeepy

Coffeepy ☕️ is a small program that prevents the system from sleeping.
Works on MacOS, Windows and Linux.

<img alt="coffeepy" src="https://github-production-user-asset-6210df.s3.amazonaws.com/22169537/253075028-9eaccaca-a567-4bd8-86c1-63d4870664ad.gif" width="600" />

## Installation

```sh
pip install -U coffeepy
```

## Usage

Simply run the program from command line
```sh
coffeepy
```

By default the program runs indefinitely. Press `Ctrl-C` to quit

Optional: You can set the time in minutes with `-t` flag. To run the program for 1 hour, use

```sh
coffeepy -t 60
```

## Python module

You can also import coffeepy as a python module

```python
import coffeepy

coffeepy.run()

# you can also specify the time in minutes
coffeepy.run(60)
```


## License

This project is licensed under the MIT [License](https://github.com/kuvaus/coffeepy/blob/main/LICENSE)
