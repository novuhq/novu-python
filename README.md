# Novu Client (Python)

[![PyPI](https://img.shields.io/pypi/v/novu-python?color=blue)](https://pypi.org/project/novu-python/)
![Tests Status](https://github.com/SpikeeLabs/novu-python/actions/workflows/.github/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/SpikeeLabs/novu-python/branch/main/graph/badge.svg?token=RON7F8QTZX)](https://codecov.io/gh/SpikeeLabs/novu-python)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/novu-python)
![PyPI - License](https://img.shields.io/pypi/l/novu-python)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

---

This project aims to provide a python wrapper for the Novu API.

> :warning: **This deposit is not officially maintained by [novuhq](https://github.com/novuhq).** The Novu software development team is currently (March 2023) thinking of using the [ferns](https://www.buildwithfern.com/) solution to create an SDK for all languages for easier maintenance. For more details on the subject or to follow the progress on the official SDK support, you can check the issue https://github.com/novuhq/novu/issues/2835.

## Install

To install this package

```shell
# Via pip
pip install novu-python

# Via poetry
poetry add novu-python
```

## Quick start

This package is a wrapper of all the resources offered by Novu, we will just start by triggering an event on Novu.

To do this, you will need to:

1. Follow Novu's procedure on how to set up your first template and keep in mind the identifier to trigger the template: https://docs.novu.co/overview/quick-start#create-a-notification-template
2. Retrieve your API key from the platform directly in the settings section: https://web.novu.co/settings
3. Play the following script:

```python
from novu.api import EventApi

event_api = EventApi("https://api.novu.co/api/", "<NOVU_API_TOKEN>")
event_api.trigger(
    name="<YOUR_TEMPLATE_NAME>",
    recipients="<YOUR_SUBSCRIBER_ID>",
    payload={},  # Your Novu payload goes here
)
```

If all is ok, this should have triggered a notification in Novu.

## Development

```bash
# install deps
poetry install

# pre-commit
poetry run pre-commit install --install-hook
poetry run pre-commit install --install-hooks --hook-type commit-msg
```
