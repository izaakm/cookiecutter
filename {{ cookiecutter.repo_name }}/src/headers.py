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

PROJECTDIR = '~/projects/{{cookiecutter.repo_name}}'
assert os.path.exists(PROJECTDIR), 'PROJECT_DIR does not exist: {}'.format(PROJECTDIR)

DATADIR = os.path.join(PROJECTDIR, 'data')
assert os.path.exists(DATADIR), 'DATADIR does not exist: {}'.format(DATADIR)

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
        args = dict(sep='\t', index_col=0)
        args.update(kwargs)
        df = pd.read_csv(path, **args)
    elif path.endswith('.csv'):
        args = dict(index_col=0)
        args.update(kwargs)
        df = pd.read_csv(path, **args)
    elif path.endswith('.xlsx'):
        args = dict(index_col=0)
        args.update(kwargs)
        df = pd.read_excel(path, **args)
    else:
        print('Unknown file extension:', path, file=sys.stderr, flush=True)
        df = None
    return df


def color_palette(palette='viridis', n_colors=6):
    '''
    This function is written to mimic `sns.color_palette`.
    It returns a list of colors in the given palette.
    Just provide the color palette that you want and the number of colors.
    '''
    
    from matplotlib.colors import Normalize
    from matplotlib.pyplot import cm

    n_ints = range(n_colors)

    minimum = min(n_ints)
    maximum = max(n_ints)

    # norm = matplotlib.colors.Normalize(vmin=minimum, vmax=maximum, clip=True)
    # mapper = plt.cm.ScalarMappable(norm=norm, cmap=plt.cm.get_cmap(palette))
    
    norm = Normalize(vmin=minimum, vmax=maximum, clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=cm.get_cmap(palette))

    # colors = []
    # for i in n_ints:
    #     colors.append(mapper.to_rgba(i))
    colors = [mapper.to_rgba(i) for i in n_ints]
    return colors


def join_columns(df, sep=' '):
    # df = md[['source_name', 'sample_case']]
    # join_columns(df)
    # join_columns(df, sep='_')
    df = df.copy()
    df = df.apply(lambda row: sep.join(row), axis=1)
    return df


# END
