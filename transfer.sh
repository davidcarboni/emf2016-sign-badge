#!/bin/bash

if [ -d /media/$USER/PYBFLASH/apps ]
then
  mkdir -p /media/$USER/PYBFLASH/apps/lights
  cp main.py /media/$USER/PYBFLASH/apps/lights/ && echo Code transferred.
else
  echo "Can't find /media/$USER/PYBFLASH/apps/ - is the device plugged in?"
fi
