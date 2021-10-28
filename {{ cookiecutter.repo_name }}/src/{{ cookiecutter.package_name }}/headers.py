import os
import re
import requests
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from glob import glob

PROJECTDIR = os.path.realpath(os.path.expanduser('~/projects/{{cookiecutter.repo_name}}'))
assert os.path.exists(PROJECTDIR), 'PROJECTDIR does not exist: {}'.format(PROJECTDIR)

DATADIR = os.path.join(PROJECTDIR, 'data')
assert os.path.exists(DATADIR), 'DATADIR does not exist: {}'.format(DATADIR)

# CACHE = os.path.join(PROJECTDIR, '_cache')

# END
