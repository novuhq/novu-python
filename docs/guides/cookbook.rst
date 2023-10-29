Cookbook
========

Changing API Requests Timeout
------------------------------

There are two ways to modify the timeout for API requests made by the :module:`requests` module:

1. **Using an Environment Variable**

   You can set an environment variable named ``NOVU_PYTHON_REQUESTS_TIMEOUT`` to specify the timeout in seconds. This variable will override all timeouts in this package.

   Example:

   .. code-block:: python

      export NOVU_PYTHON_REQUESTS_TIMEOUT=60

2. **Using API Constructor**

   You can pass the `request_timeout` parameter directly to the API constructor.

   Example:

   .. code-block:: python

      EventApi(..., ..., request_timeout=60).trigger_bulk(...)

Taking Control Over the Requests Session
-----------------------------------------

At times, you may want to employ advanced usage involving a `requests.Session`.

By default, a session is created for every API request. However, you can also provide your own session and reuse it as needed.

For instance, let's set up an automatic retry mechanism for requests when the API responds with HTTP codes 502, 503, or 504. To do this, follow these steps:

1. Instantiate a :class:`~requests.Session` from the :module:`requests` module.
2. Mount a :class:`~requests.adapters.HTTPAdapter` with a custom retry strategy using a :class:`~requests.adapters.Retry`.
3. Inject the session into the API constructor.

Example:

.. code-block:: python

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
