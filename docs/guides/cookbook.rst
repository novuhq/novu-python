Cookbook
========

How to Change API Requests Timeout?
-----------------------------------

You can adjust the timeout for API requests made with the `requests` module in two ways:

Using an Environment Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the environment variable `NOVU_PYTHON_REQUESTS_TIMEOUT` to define the timeout in seconds. This will override all timeouts in this package.

Directly in API Constructor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pass `requests_timeout` as a keyword argument during initialization.

Example::

    EventApi(..., ..., request_timeout=60).trigger_bulk(...)

How to Take Control Over the Session of ``requests``?
------------------------------------------------------

Sometimes, you may need to perform advanced operations using a ``requests.Session``.

By default, a session is created for each API request. However, you can also provide your own session for reuse.

Here's an example of setting up an automatic retry mechanism for requests with specific HTTP status codes (502, 503, 504)::

    from requests import Session
    from requests.adapters import HTTPAdapter, Retry

    from novu.api import EventApi

    session = Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount("https://api.novu.co", HTTPAdapter(max_retries=retries))

    event_api = EventApi("https://api.novu.co/api/", "<NOVU_API_TOKEN>", session=session)
    event_api.trigger(
        name="<YOUR_TEMPLATE_NAME>",
        recipients="<YOUR_SUBSCRIBER_ID>",
        payload={},  # Your Novu payload goes here
    )

This example demonstrates how to create a custom session and use it with the Event API.

In a more approachable way, we refer to this solution as "Customer Identity Access Management (CIAM)" or simply, the "Customer Identity Solution."

Subscribe to us right away to receive up-to-date information about the Logto Cloud (SaaS) as well as in-time feature updates.
