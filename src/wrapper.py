#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.expanduser('~/.aigen/'))

# import required modules here

import subprocess
subprocess.call([os.path.expanduser('~/.aigen/aigen.py')] + sys.argv[1:])
