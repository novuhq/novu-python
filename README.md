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
ßß
# Via poetry
poetry add novu
```

## Contents

- [Install](#install)
- [Quick start](#quick-start)
- [Code Snippet Examples](#code-snippet-examples)
  - [Events](#events)
  - [Subscribers](#subscribers)
  - [Topics](#topics)
  - [Feeds](#feeds)
  - [Environments](#environments)
- [Go further](#go-further)
- [Development](#development)

## Quick start

This package is a wrapper of all the resources offered by Novu, we will just start by triggering an event on Novu.

To do this, you will need to:

1. Create your first notification workflow and keep in mind the identifier to trigger the workflow: https://docs.novu.co/overview/quickstart/general-quickstart#create-a-workflow
2. Retrieve your API key from the Novu dashboard directly in the settings section: https://web.novu.co/settings
3. Write code to trigger your first event:

```python
from novu.api import EventApi

event_api = EventApi("https://api.novu.co", "<NOVU_API_KEY>")
event_api.trigger(
    name="<YOUR_WORKFLOW_ID>",  # The workflow ID is the slug of the workflow name. It can be found on the workflow page.
    recipients="<YOUR_SUBSCRIBER_ID>",
    payload={},  # Your Novu payload goes here
)
```

This will trigger a notification to the subscribers.

## Code Snippet Examples

### Events

Firstly, make imports and declare the needed variables this way:

```python
from novu.api import EventApi

url = "https://api.novu.co"
api_key = "<NOVU_API_KEY>"

# You can sign up on https://web.novu.co to get your API key from https://web.novu.co/settings
```

**Trigger an event** - Send notification to subscribers:

```python
from novu.api import EventApi

novu = EventApi(url, api_key).trigger(
    name="digest-workflow-example",  # This is the Workflow ID. It can be found on the workflow page.
    recipients="<SUBSCRIBER_IDENTIFIER>", # The subscriber ID can be gotten from the dashboard.
    payload={},  # Your custom Novu payload goes here
)
```

**Bulk Trigger events** - Trigger multiple events at once:

```python
from novu.dto.event import InputEventDto
from novu.api import EventApi

url = "https://api.novu.co"
api_key = "<NOVU_API_KEY>"

event_1 = InputEventDto(
    name="digest-workflow-example",  # The workflow ID is the slug of the workflow name. It can be found on the workflow page.
    recipients="<SUBSCRIBER_IDENTIFIER>",
    payload={},  # Your custom Novu payload goes here
)
event_2 = InputEventDto(
    name="digest-workflow-example",
    recipients="<SUBSCRIBER_IDENTIFIER>",
    payload={},
)

novu = EventApi("https://api.novu.co", api_key).trigger_bulk(events=[event1, event2])
```

**Broadcast to all current subscribers:**

```python
novu = EventApi(url, api_key).broadcast(
    name="digest-workflow-example",
    payload={"customVariable": "value"},  # Optional
)
```

### Subscribers

```python
from novu.dto.subscriber import SubscriberDto
from novu.api.subscriber import SubscriberApi

url = "https://api.novu.co"
api_key = "<NOVU_API_KEY>"

# Define a subscriber instance
subscriber = SubscriberDto(
    email="novu_user@mail.com",
    subscriber_id="82a48af6ac82b3cc2157b57f", #This is what the subscriber_id looks like
    first_name="",  # Optional
    last_name="",  # Optional
    phone="",  # Optional
    avatar="",  # Optional
)

# Create a subscriber
novu = SubscriberApi(url, api_key).create(subscriber)

# Get a subscriber
novu = SubscriberApi(url, api_key).get(subscriber_id)

# Get list of subscribers
novu = SubscriberApi(url, api_key).list()
```

### Topics

```python
from novu.api import TopicApi

url = "<NOVU_URL>"
api_key = "<NOVU_API_KEY>"

# Create a topic
novu = TopicApi(url, api_key).create(
    key="new-customers", name="New business customers"
)

# Get a topic
novu = TopicApi(url, api_key).get(key="new-customers")

# List topics
novu = TopicApi(url, api_key).list()

# Rename a topic
novu = TopicApi(url, api_key).rename(key="new-customers", name="New business customers")

# Subscribe a list of subscribers to a topic
novu = TopicApi(url, api_key).subscribe(key="old-customers", subscribers="<LIST_OF_SUBSCRIBER_IDs>")

# Unsubscribe a list of subscribers from a topic
novu = TopicApi(url, api_key).unsubscribe(key="old-customers", subscribers="<LIST_OF_SUBSCRIBER_IDs>")

```

### Feeds

```python
from novu.api.feed import FeedApi

url = "<NOVU_URL>"
api_key = "<NOVU_API_KEY>"

# Create a Feed
novu = FeedApi(url, api_key).create(name="<SUPPLY_NAME_FOR_FEED>")

# Delete a Feed
novu = FeedApi(url, api_key).delete(feed_id="<FEED_IDENTIFIER")

# List feeds
novu = FeedApi(url, api_key).list()
```

### Environments

```python
from novu.api.environment import EnvironmentApi

url = "<NOVU_URL>"
api_key = "<NOVU_API_KEY>"

# Create an Environment
novu = EnvironmentApi(url, api_key).create(
    name="<INSERT_NAME>", 
    parent_id="<INSERT_PARENT_ID>" # Optional. Defaults to None
)

# # List existing environments
novu = EnvironmentApi(url, api_key).list()

# # Get the current environment
novu = EnvironmentApi(url, api_key).current()

# # Retrieve an environment's API_KEY
novu = EnvironmentApi(url, api_key).api_keys()

```

## Go further

After a quick start with the SDK, you'll quickly get to grips with the advanced use of the SDK and the other APIs available.

For this purpose, documentation is available here: https://novu-python.readthedocs.io/

## Development

```bash
# install deps
poetry install

# pre-commit
poetry run pre-commit install --install-hook
poetry run pre-commit install --install-hooks --hook-type commit-msg
```
