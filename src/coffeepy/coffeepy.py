#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
import sys
import subprocess
import time
import argparse
import os
import warnings
import jeepney
from jeepney.io.blocking import open_dbus_connection


animation = [
    "  ☕️   ",
    " ☁️☕️   ",
    "  ☕️   ",
    "  ☕️☁️  ",
    " ☁️☕️   ",
    "  ☕️   ",
]

ascii_animation = [
    "  |   ",
    "  /   ",
    "  -   ",
    "  \\   ",
]

def display_animation(animation=animation):
    for frame in animation:
        print('\r' + frame, end='')
        time.sleep(0.5)  # Adjust the delay time as desired

def get_version(package):
    if sys.version_info >= (3, 8):
        from importlib.metadata import version
        return version(package)
    else:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            import pkg_resources
            return pkg_resources.get_distribution(package).version


# On macOS check caffeinate
def check_caffeinate():
    try:
        subprocess.check_output(['which', 'caffeinate'])
        return True
    except subprocess.CalledProcessError:
        return False

# On Windows check if we use Windows Terminal
def check_windows_terminal():
    if ('win32' in sys.platform) and (os.environ.get("WT_SESSION") is not None):
        return True
    else:
        return False

# On Linux use jeepney
try:
    connection = open_dbus_connection(bus="SESSION")
except Exception as e:
    if 'linux' in sys.platform:
        print("Could not set DBUS SESSION")
        connection = None

proxy = jeepney.DBusAddress('/org/freedesktop/ScreenSaver', bus_name='org.freedesktop.ScreenSaver', interface='org.freedesktop.ScreenSaver')

def set_dbus_awake():
    msg = jeepney.new_method_call(proxy, "Inhibit", "ss", ("coffeepy", "wakelock active"))
    reply = connection.send_and_get_reply(msg)
    cookie = reply.body[0]
    return cookie

def unset_dbus_awake(cookie):
    if cookie is None:
        return
    else:
        msg = jeepney.new_method_call(proxy, "UnInhibit", "u", (cookie,))
        connection.send_and_get_reply(msg)

#def check_x11():
#    try:
#        subprocess.check_output(['which', 'xset'])
#        return True
#    except subprocess.CalledProcessError:
#        print("You need to install either \'caffeinate\' or \'x11-xserver-utils\' package for this program to run")
#        return False


def parse_args(args=None):

    coffee_emoji = "☕️"
    if 'win32' in sys.platform and not check_windows_terminal():
        coffee_emoji = ""

    description = 'Coffeepy (v'+get_version('coffeepy')+') '+coffee_emoji+""" prevents the system from sleeping.
You can set the time with -t flag
Made by kuvaus"""

    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-t', '--time', type=float, default=0, help='Optional: Duration of animation in minutes. Use 0 for indefinite duration')
    parser.add_argument('-a', '--no-animation', action='store_true', help='Optional: Disable animation')

    return parser.parse_args(args)
    
def run(runtime=0, no_animation=False):

    args = None
    if runtime > 0 or no_animation:
        args = ['-t', str(runtime)]
        if no_animation:
            args.append('-a')

    args = parse_args(args)
        
    if args.time == 0:
        duration = float('inf')  # Set duration to infinity
    else:
        duration = args.time * 60  # Convert minutes to seconds

    proc = None
    cookie = None

    if 'darwin' in sys.platform:
        print('Running \'coffeepy\' on MacOS to prevent the system from sleeping')
        proc = subprocess.Popen(['caffeinate', '-dims'])

    elif 'linux' in sys.platform:
        print('Running \'coffeepy\' on Linux to prevent the system from sleeping')
        if check_caffeinate():
            proc = subprocess.Popen(['caffeinate', '-dims'])
        else:
            # Keep system awake using DBUS
            if connection is None:
                print("You need to install either \'dbus\' or \'caffeinate\' package for this program to run")
                sys.exit(0)
            cookie = set_dbus_awake()
            
            #if cookie is None:
            #    if check_x11():
            #        subprocess.Popen(['xset', 's', 'off'])
            #        subprocess.Popen(['xset', '-dpms'])
            #    else:
            #        sys.exit(0)

    elif 'win32' in sys.platform:
        print('Running \'coffeepy\' on Windows to prevent the system from sleeping')
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

    print('Press Ctrl-C to quit')
    
    try:
        start_time = time.time()
        while time.time() - start_time < duration or duration == float('inf'):
            if not args.no_animation:
                if 'win32' in sys.platform and not check_windows_terminal():
                    display_animation(ascii_animation)
                else:
                    display_animation()
            else:
                time.sleep(1)

    except KeyboardInterrupt:
        print('\nExiting')

    finally:
        if proc:
            proc.terminate()
        if 'linux' in sys.platform and not check_caffeinate():
            unset_dbus_awake(cookie)
            # Reset xset settings
            #subprocess.Popen(['xset', 's', 'on'])
            #subprocess.Popen(['xset', '+dpms'])
        if 'win32' in sys.platform:
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)


if __name__ == "__main__":
    run()
