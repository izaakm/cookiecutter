import os
import re
import requests
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from glob import glob

from statsmodels.sandbox.stats.multicomp import multipletests

PROJECTDIR = os.path.expanduser('~/path/to/projects')
assert os.path.exists(PROJECT_DIR), 'PROJECT_DIR does not exist: {}'.format(PROJECT_DIR)

DATADIR = os.path.join(PROJECTDIR, 'data')
assert os.path.exists(DATADIR), 'DATADIR does not exist: {}'.format(DATADIR)

# 'processed/counted/tpmcalculator/merged/counts-exon.tsv'
# 'processed/counted/tpmcalculator/merged/counts-total.tsv'
# 'processed/counted/tpmcalculator/merged/genelengths-exon.tsv'
# 'processed/counted/tpmcalculator/merged/genelengths-total.tsv'
# 'processed/counted/tpmcalculator/merged/tpm-exon.tsv'
# 'processed/counted/tpmcalculator/merged/tpm-total.tsv'

DESIGN_FILE = os.path.join(DATADIR, 'design.tsv')
COUNTS_FILE = os.path.join(DATADIR, 'counts.tsv')
TPM_FILE = os.path.join(DATADIR, 'tpm.tsv')


def dirname_basename_ext(path):
    dirname, basename = os.path.split(path)
    # if '.' in basename:
    #     base, ext = os.path.splitext(basename)
    # else:
    #     base = basename
    #     ext = None
    base, ext = os.path.splitext(basename)
    return (dirname, base, ext)


def head(dataframe, rows=3):
    '''
    PLACEHOLDER -- NOT YET IMPLEMENTED.

    Helper to display dtypes with `pd.DataFrame.head()`.
    '''
    # Merge dtypes and column names, then print/return.
    pass


def read_data(path, **kwargs):
    if path.endswith('.pkl'):
        df = pd.read_pickle(path, **kwargs)
    elif path.endswith('.tsv') or path.endswith('.txt'):
        df = pd.read_csv(path, sep='\t', **kwargs)
    elif path.endswith('.csv'):
        df = pd.read_csv(path, **kwargs)
    elif path.endswith('.xlsx'):
        df = pd.read_excel(path, **kwargs)
    else:
        print('Unknown file extension:', path, file=sys.stderr, flush=True)
        df = None
    return df


# END.
