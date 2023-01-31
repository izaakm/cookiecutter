% My Cookiecutter

Forked from [Cookiecutter Data Science][1617159b] ([GitHub][b352f0b8]):

> *A logical, reasonably standardized, but flexible project structure for doing
> and sharing data science work.*

> **New version of Cookiecutter Data Science**
> 
> Cookiecutter data science is moving to v2 soon, which will entail using
> the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
> will continue to work, and this version of the template will still be available.
> To use the legacy template, you will need to explicitly use `-c v1` to select it.
> Please update any scripts/automation you have to append the `-c v1` option (as above),
> which is available now.


Requires
========

 - Python 2.7 or 3.5+
 - [Cookiecutter Python package][install] >= 1.4.0


Create a new project directory using this template
==================================================

Install Cookiecutter with pip:

```sh
$ pip install cookiecutter
```

or conda:

```sh
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

```sh
$ cookiecutter https://github.com/izaakm/cookiecutter
```

Follow the prompts, and Cookiecutter will automatically produce a project like
this:

```
├── LICENSE
├── README.md       <- The top-level README for developers using this project.
├── data            <- Data directory (data is NOT tracked by git!!!)
├── docs            <- A default Sphinx project; see sphinx-doc.org for details
├── models          <- Trained and serialized models, model predictions, or model summaries
├── references      <- Data dictionaries, manuals, and all other explanatory materials.
├── reports         <- Generated analysis as HTML, PDF, LaTeX, etc.
├── environment.yml <- Dependencies for your project's conda environment.
├── setup.py        <- Install the code for your project with `pip install -e`.
├── src             <- Source code for your project.
└── tox.ini         <- tox file with settings for running tox; see tox.readthedocs.io
```


Development
===========

Installing development requirements
-----------------------------------

```sh
$ pip install -r requirements.txt
```


Running the tests
-----------------

```sh
$ py.test tests
```


<!-- LINKS -->

[b352f0b8]: http://drivendata.github.io/cookiecutter-data-science/
[1617159b]: https://github.com/drivendata/cookiecutter-data-science
[install]: http://cookiecutter.readthedocs.org/en/latest/installation.html

<!-- END -->
