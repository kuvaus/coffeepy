
from importlib.metadata import version

import ctypes
import sys
import subprocess
import time
import argparse
import os

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


def check_caffeinate():
    try:
        subprocess.check_output(['which', 'caffeinate'])
        return True
    except subprocess.CalledProcessError:
        return False

def check_windows_terminal():
    if 'win32' in sys.platform:
        if os.environ.get("WT_SESSION") is not None:
            return True
        else:
            return False
    else:
        return False

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Coffeepy (v'+version('coffeepy')+') ☕️ prevents the system from sleeping.\n'
                                                 'You can set the time with -t flag\n'
                                                 'Made by kuvaus',
                                                 formatter_class=argparse.RawTextHelpFormatter)

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

    if 'darwin' in sys.platform:
        print('Running \'coffeepy\' on MacOS to prevent the system from sleeping')
        proc = subprocess.Popen(['caffeinate', '-dims'])

    elif 'linux' in sys.platform:
        print('Running \'coffeepy\' on Linux to prevent the system from sleeping')
        if check_caffeinate():
            proc = subprocess.Popen(['caffeinate', '-dims'])
        else:
            subprocess.Popen(['xset', 's', 'off'])
            subprocess.Popen(['xset', '-dpms'])

    elif 'win32' in sys.platform:
        print('Running \'coffeepy\' on Windows to prevent the system from sleeping')
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

    print('Press Ctrl-C to quit')
    
    try:
        start_time = time.time()
        while time.time() - start_time < duration or duration == float('inf'):
            if not args.no_animation:
                if 'win32' in sys.platform:
                    if check_windows_terminal() == True:
                        display_animation()
                    else:
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
            # Reset xset settings
            subprocess.Popen(['xset', 's', 'on'])
            subprocess.Popen(['xset', '+dpms'])
        if 'win32' in sys.platform:
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
        #sys.exit(0)


if __name__ == "__main__":
    run()
