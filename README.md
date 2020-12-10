# Interview project for TinyClues MLE Internship

## Introduction

This is a coding environnement for recommender systems. It should be flexible enough to use it for other types of datasets, providing you put the data into the right format.

See the **readme.ipynb** file for more information about my results about this coding challenge.

## Setup the environment

Run the following commands in your development environment

```bash
$ pip install pipenv
$ pipenv install
```

## Make tests

Run the following commands in your development environment

```bash
$ make tests
```

To see the coverage of the code, you can just run this command:

```bash
$ make coverage
```

## Lint the code

You can check if the code is written is a good way by using the following command:

```bash
$ make lint
```

**This uses pylint, mypy and flake8**, so we have also type checking !
