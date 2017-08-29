#!/bin/sh
  date > "date.txt"
  uptime > "uptime.txt"
  grep "model name" /proc/cpuinfo > "cpuinfo.txt"
  top -n 1 -b > "top.txt"
  uname -mrs > "version.txt"

