""" setup context for tests """

import os
import sys


path = os.path.join(os.path.dirname(__file__), '..')
abspath = os.path.abspath(path)
sys.path.insert(0, abspath)
