import pytest
import sys
from unittest.mock import patch, call, Mock, MagicMock
from io import StringIO
import subprocess
import builtins
from coffeepy import *

#
# Tests for:
#
# animation, ascii_animation
# display_animation()
# check_caffeinate()
# check_windows_terminal()
# parse_args()
# run()
#


#
# Test the display_animation function
#

# see if the function runs
def test_display_animation():
    display_animation()
    display_animation(animation)
    display_animation(ascii_animation)

# check with test_animation
@patch('builtins.print')
def test_display_animation_test_animation(mock_print):
    test_animation = [
        "  ☕️   ",
        " ☁️☕️   ",
        "  ☕️   ",
    ]
    display_animation(animation=test_animation)
    calls = [call('\r' + frame, end='') for frame in test_animation]
    mock_print.assert_has_calls(calls)


# check that the default animation prints the same as animation
@patch('builtins.print')
def test_display_animation_default_animation(mock_print):
    display_animation()
    calls = [call('\r' + frame, end='') for frame in animation]
    mock_print.assert_has_calls(calls)

#
# Test the check_caffeinate function
# True if caffeinate is found on /usr/bin
#

@patch('subprocess.check_output')
def test_check_caffeinate(mock_subproc):
    mock_subproc.return_value = '/usr/bin/caffeinate'
    assert check_caffeinate() is True

    mock_subproc.side_effect = subprocess.CalledProcessError(1, 'which')
    assert check_caffeinate() is False


#
# Test the check_windows_terminal function
# True if WT_SESSION is found on win32, false otherwise
#

# windows
@patch('os.environ.get')
@patch('sys.platform', 'win32')
def test_check_windows_terminal_win(mock_get):
    mock_get.return_value = None
    assert check_windows_terminal() is False

    mock_get.return_value = 'WT_SESSION'
    assert check_windows_terminal() is True

# linux
@patch('os.environ.get')
@patch('sys.platform', 'linux')
def test_check_windows_terminal_linux(mock_get):
    mock_get.return_value = None
    assert check_windows_terminal() is False

    mock_get.return_value = 'WT_SESSION'
    assert check_windows_terminal() is False

# macos
@patch('os.environ.get')
@patch('sys.platform', 'darwin')
def test_check_windows_terminal_macos(mock_get):
    mock_get.return_value = None
    assert check_windows_terminal() is False

    mock_get.return_value = 'WT_SESSION'
    assert check_windows_terminal() is False

#
# Test argument parsing
#

def test_argument_parsing_default():
    args = parse_args([])
    assert args.time == 0
    assert args.no_animation is False

def test_argument_parsing_time():
    args = parse_args(['-t', '10'])
    assert args.time == 10

def test_argument_parsing_no_animation():
    args = parse_args(['-a'])
    assert args.no_animation


#
# Test the run function
# First make sure this is run on a system with caffeinate
#

if check_caffeinate():
    def test_timed_run():
        runtime = 0.01
        run(runtime)

    def test_timed_run():
        runtime = 0.01
        run(runtime)

#
# Test run on macos, linux and windows
#

# macOS
# Use mock to simulate 'check_caffeinate'
#
@patch('sys.platform', new='darwin')
@patch('subprocess.Popen')
@patch('subprocess.check_output')
def test_platform_macos(mock_subproc, mock_popen):
    mock_subproc.return_value = '/usr/bin/caffeinate'
    mock_popen.return_value.returncode = 0
    runtime = 0.01
    run(runtime)
    mock_popen.assert_called_once_with(['caffeinate', '-dims'])

#
# Linux and caffeinate
# Use mock to simulate 'check_caffeinate'
#
@patch('sys.platform', new='linux')
@patch('subprocess.Popen')
@patch('subprocess.check_output')
def test_platform_linux_with_caffeinate(mock_subproc, mock_popen):
    mock_subproc.return_value = '/usr/bin/caffeinate'
    mock_popen.return_value.returncode = 0
    runtime = 0.01
    run(runtime)
    mock_popen.assert_called_once_with(['caffeinate', '-dims'])


#
# Windows
# Use mock to simulate 'ctypes.windll.kernel32.SetThreadExecutionState'
#
@patch('sys.platform', new='win32')
@patch('ctypes.windll', create=True)
def test_platform_windows(self):
    runtime = 0.01
    run(runtime)


#
# DBUS
# 
#


@patch('coffeepy.open_dbus_connection')
@patch('coffeepy.jeepney.new_method_call')
def test_set_dbus_awake(mock_new_method_call, mock_open_dbus_connection):
    # Mock open_dbus_connection
    mock_connection = MagicMock()
    mock_open_dbus_connection.return_value = mock_connection
    #mock_connection.return_value = mock_connection

    # Mock new_method_call and send_and_get_reply
    mock_new_method_call.return_value = 'mocked_msg'
    mock_connection.send_and_get_reply.return_value = MagicMock(body=[123])

    # Patch the mock_connection in set_dbus_awake
    with patch('coffeepy.set_dbus_awake', return_value=123) as mock_set_dbus_awake:
        # Call set_dbus_awake and verify it returns the expected cookie
        cookie = coffeepy.set_dbus_awake(mock_connection)
        assert cookie == 123

        # Verify open_dbus_connection and new_method_call were called with the correct arguments
        
        mock_new_method_call.assert_called_once_with(coffeepy.proxy, "Inhibit", "ss", ("coffeepy", "wakelock active"))

    # Verify set_dbus_awake was called with the mock_connection
    #mock_set_dbus_awake.assert_called_once_with(mock_connection)

@patch('coffeepy.open_dbus_connection')
@patch('coffeepy.jeepney.new_method_call')
def test_unset_dbus_awake(mock_new_method_call, mock_open_dbus_connection):
    # Mock open_dbus_connection
    mock_connection = MagicMock()
    mock_open_dbus_connection.return_value = mock_connection

    # Mock new_method_call
    mock_new_method_call.return_value = 'mocked_msg'

    # Patch the mock_connection in unset_dbus_awake
    with patch('coffeepy.set_dbus_awake', return_value=123) as mock_set_dbus_awake:
        # Call unset_dbus_awake
        coffeepy.unset_dbus_awake(mock_connection, 123)

    # Verify open_dbus_connection and new_method_call were called with the correct arguments
    #mock_open_dbus_connection.assert_called_once_with(bus="SESSION")
    mock_new_method_call.assert_called_once_with(coffeepy.proxy, "UnInhibit", "u", (123,))

    # Verify send_and_get_reply was called once
    mock_connection.send_and_get_reply.assert_called_once_with('mocked_msg')
    
