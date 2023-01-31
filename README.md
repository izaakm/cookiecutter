My Cookiecutter
================================================================================

*A logical, reasonably standardized, but flexible project structure for doing
and sharing data science work.*

- forked from [Cookiecutter Data Science][1617159b] ([Project homepage][b352f0b8])


Requirements to use the cookiecutter template:
--------------------------------------------------------------------------------

 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

```sh
$ pip install cookiecutter
```

or

```sh
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


To start a new project, like *this* one:
--------------------------------------------------------------------------------


    cookiecutter https://github.com/izaakm/cookiecutter

### New version of Cookiecutter Data Science
------------
Cookiecutter data science is moving to v2 soon, which will entail using
the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
will continue to work, and this version of the template will still be available.
To use the legacy template, you will need to explicitly use `-c v1` to select it.
Please update any scripts/automation you have to append the `-c v1` option (as above),
which is available now.
>>>>>>> upstream/master


The resulting directory structure
--------------------------------------------------------------------------------


### The resulting directory structure
------------

The directory structure of your new project looks like this: 


```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   └── processed      <- The final, canonical data sets for modeling.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│   └── methods        <- Both experimental and computational methods in plain english (no code).
│
├── project            <- Project description, timeline, contributors, etc.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Make this project pip installable with `pip install -e`.
│                         Run `pip install -e .` in the root of the project to install `src` to the current environment.
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   ├── load.py
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

<!-- ## Contributing -->
<!-- We welcome contributions! [See the docs for -->
<!-- guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing). -->

Installing development requirements
--------------------------------------------------------------------------------

    pip install -r requirements.txt


Running the tests
--------------------------------------------------------------------------------

    py.test tests


<!-- links -->

[b352f0b8]: http://drivendata.github.io/cookiecutter-data-science/
[1617159b]: https://github.com/drivendata/cookiecutter-data-science

<!-- END -->
