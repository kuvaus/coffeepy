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

Optional: You can set the time in minutes with `-t` or `--time` flag. For example, to run the program for 1 hour, use

```sh
coffeepy -t 60
```
You can also disable animation with `-a` or `--no-animation` flag.
```sh
coffeepy -a
```
You can view the full parameter list with `-h` or `--help`.

## Python module

You can also import coffeepy as a python module

```python
import coffeepy

coffeepy.run()
```

Optional settings when run as a python module:

```python
import coffeepy

# you can also specify the time in minutes
# if no time is provided or time = 0, the program will run indefinitely
coffeepy.run(60)

# to disable animation when run as a module, you can set the second argument to True
coffeepy.run(0, True)
```


## License

This project is licensed under the MIT [License](https://github.com/kuvaus/coffeepy/blob/main/LICENSE)
