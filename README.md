# Python Novu SDK

[![PyPI](https://img.shields.io/pypi/v/novu?color=blue)](https://pypi.org/project/novu/)
![Tests Status](https://github.com/novuhq/novu-python/actions/workflows/.github/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/novuhq/novu-python/branch/main/graph/badge.svg?token=RON7F8QTZX)](https://codecov.io/gh/novuhq/novu-python)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/novu)
![PyPI - License](https://img.shields.io/pypi/l/novu)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

---

The [Python Novu](https://novu.co) SDK and package provides a fluent and expressive interface for interacting with [Novu's API](https://api.novu.co/api) and managing notifications.

## Install

To install this package

```shell
# Via pip
pip install novu

# Via poetry
poetry add novu
```

## Quick start

This package is a wrapper of all the resources offered by Novu, we will just start by triggering an event on Novu.

To do this, you will need to:

1. Create your first notification template and keep in mind the identifier to trigger the template: https://docs.novu.co/overview/quick-start#create-a-notification-template
2. Retrieve your API key from the Novu dashboard directly in the settings section: https://web.novu.co/settings
3. Write code to trigger your first event:

```python
from novu.api import EventApi

event_api = EventApi("https://api.novu.co/api/", "<NOVU_API_TOKEN>")
event_api.trigger(
    name="<YOUR_TEMPLATE_NAME>",
    recipients="<YOUR_SUBSCRIBER_ID>",
    payload={},  # Your Novu payload goes here
)
```

This will trigger a notification to the subscribers.

## Development

```bash
# install deps
poetry install

# pre-commit
poetry run pre-commit install --install-hook
poetry run pre-commit install --install-hooks --hook-type commit-msg
```
