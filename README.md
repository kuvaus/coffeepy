# Coffeepy

Coffeepy ☕️ is a small program that prevents the system from sleeping.
Works on MacOS, Windows and Linux.

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
```


## License

This project is licensed under the MIT [License](https://github.com/kuvaus/coffeepy/blob/main/LICENSE)


