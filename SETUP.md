# Procedure for setting up a deposit

This document deals with the different actions to be taken on github and
related third party services to set up this repository correctly.

> :warning: This documentation is written for hosting on Github. If you want
> to host this repository via another manager, you will have to rethink the
> CI/CD part related to the repository.

## Prerequisites

- This guide considers the project hosted by a github repository.
- You have administrator access to this repository.

## Prepare third party services

### CodeCov

CodeCov provides highly integrated tools for developers and engineering leaders to gain actionable visibility into their code coverage.
See https://about.codecov.io/ for more details.

We use this third party service to make the coverage report public and readable.

To set up this service, you need to:

- Connect to the CodeCov website
- Connect CodeCov and its Github organization
- Click on setup this repository
- Copy the token provided by them and register it in the variables of the linked Github repository.

### PyPi

The Python Package Index (PyPI) is a repository of software for the Python programming language.
See https://pypi.org/ for more details.

We use this third party to store and provide to python use the python code in a package.

To set up this service, you need to:

- Register on PyPI (preferably by creating an account with an anonymous address of your organization)
- Log in to PyPI
- Go to "Account settings
- Scroll down to the API Tokens section
- Create a first temporary token with a full scope for the first registration of your package
- Register this token in "Repository secrets" on your Github repository (variable `PYPI_TOKEN`)
- Run the CI/CD on one of the Release tags (example: v1.1.0)
- Wait for the end of the CI/CD
- Check the PyPi account and confirm that the project has been created
- Delete the temporary token
- Create a new token with the scope only on the project
- Save it in the "Repository secrets" section by modifying the previous value.

### ReadTheDocs

Read the Docs simplifies software documentation by automating the compilation, versioning and hosting of your documentation.
See https://readthedocs.org/ for more details.

To set up this service, you need to:

- Register on the read the docs website
- Click on "Import a project"
- Click on "Import manually"
- Fill in the project name ("novu")
- Enter the URL of the project
- Enter the default branch ("main")
- Click on "Next"

Knowing that there is a file to tell readthedocs at the root of the project, it should know how to import and publish the documentation.

## Configure the repository

Once all the integrations are prepared, we can configure the repository.

### General

In the general section, it is important to uncheck Pull Requests with Merge Commits to avoid losing the semantic release system

### Branches

It is necessary to add 2 branch protections for the alpha and hand branches:

- [x] Require linear history
- [x] Require a pull request before merging
- [x] Require approvals (1 at least)
- [x] Dismiss stale pull request approvals when new commits are pushed
- [x] Require conversation resolution before merging
- [x] Require status checks to pass before merging
- [x] Require branches to be up to date before merging
