
## Changelog

#### [Upcoming](https://github.com/kuvaus/coffeepy/compare/v0.2.1...HEAD)

#### [v0.2.1](https://github.com/kuvaus/coffeepy/releases/tag/v0.2.1)

> 24 July 2023

- Add ability to reset the system idle timer on Windows
- This prevents computer from going to sleep even if no other programs are running

#### [v0.2.0](https://github.com/kuvaus/coffeepy/releases/tag/v0.2.0)

> 23 July 2023

- Simplify dependencies

#### [v0.1.9](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.9)

> 23 July 2023

- Finally works properly on various linux systems
- Use `DBUS` on linux to prevent system from sleeping  [`#1`](https://github.com/kuvaus/coffeepy/pull/1)
- Use `systemd` on linux as a fallback method
- Deprecate old linux method of using `xset`
- Automatic release notes
- Improve tests

#### [v0.1.8](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.8)

> 22 July 2023

- Fix `--help` on windows systems without unicode support
- Better error handling on Linux
- Add Python 3.7 support

#### [v0.1.7](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.7)

> 16 July 2023

- Significantly improved performance when animation is turned off
- Improve tests

#### [v0.1.6](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.6)

> 14 July 2023

- Corrected Python requirements to 3.8 and newer
- Time can now be a float so you can run it more accurately
- Add tests. Run the tests with `pytest`

#### [v0.1.5](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.5)

> 13 July 2023

- Improve terminal checking function

#### [v0.1.4](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.4)

> 13 July 2023

- Fix bug in checking new Windows Terminal
- Add ability to specify time=0 when run as a module
- Add ability to disable animation when run as a module

#### [v0.1.3](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.3)

> 13 July 2023

- Add `--no-animation` flag
- Add ascii animation on Windows Powershell
- Fix duration bug from 0.1.2

#### [v0.1.2](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.2)

> 13 July 2023

- Ability to set duration when run as a python module
- Add .whl and .tar.gz to Github releases

#### [v0.1.1](https://github.com/kuvaus/coffeepy/releases/tag/v0.1.1)

> 12 July 2023

- Automatic Pypi distribution with Github actions
- Better project structure

#### v0.1.0

> 12 July 2023

- First version
