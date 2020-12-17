#!/bin/sh
### BEGIN INIT INFO
# Provides:          lights-off.sh
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Disable the power and status led.
# Description:       Disable the power and status led.
### END INIT INFO

sudo sh -c 'echo none > /sys/class/leds/led0/trigger'
sudo sh -c 'echo none > /sys/class/leds/led1/trigger'
