Cookbook
========

How to change API requests timeout?
-----------------------------------

There are two ways to change the timeout of the :module:`requests` module that makes the API calls for you:

* Via an environment variable named ``NOVU_PYTHON_REQUESTS_TIMEOUT``.
  You can define it in seconds and it will overloads all timeouts in this package.
* Via the API constructor directly, passing :attr:`~novu.api.base.Api.requests_timeout` in keywords arguments during the initialisation.

.. code-block:: python

    EventApi(...,...,request_timeout=60).trigger_bulk(...)

How to add retry mechanism for API call?
----------------------------------------

In order to enhance the resilience and reliability of the SDK, we provide Exponential Retry mechanism to retry failed API requests.

This means that the waiting time between each retry is multiplied by a factor that increases with each retry.
For example, the first retry may wait for 1 second, the second retry may wait for 2 seconds, the third retry may wait for 4 seconds, and so on until it stops at nth retry.
You can configure this interval using ``initial_delay``, ``wait_min``, ``wait_max``, and ``retry_max`` attributes.

This mechanism reduces the number of failed requests and prevents server overload by gradually increasing the waiting time between retries
and use an ``Idempotency-Key`` HTTP Header to ensure the idempotent processing of requests.

To enable this feature, first create a :class:`~novu.api.base.RetryConfig` class and use it in API constructor.

.. code-block:: python

    from novu.api import EventApi
    from novu.api.base import RetryConfig

    retry_config = RetryConfig(initial_delay=1, wait_min=2, wait_max=100, retry_max=6)

    event_api = EventApi("https://api.novu.co", "<NOVU_API_TOKEN>", retry_config=retry_config)
    event_api.trigger(
        name="<YOUR_TEMPLATE_NAME>",
        recipients="<YOUR_SUBSCRIBER_ID>",
        payload={},  # Your Novu payload goes here
    )

How to take control over the session of ``requests``?
-----------------------------------------------------

Sometime, you may want to setup advanced usage involving the use of a ``requests`` :class:`~requests.Session`.

By default, a session is declared for every request you make to the API, but you can also
provide your own session and reuse it over and over again.

To illustrate this use case, let's take the example of setting up an automatic retry mechanism on
requests when the API responds with a 502, 503 or 504 HTTP codes.

To do this, before initializing the Event API, we will first instantiate a :class:`~requests.Session` from the
:module:`requests` module, then we will inject it into the keywords arguments of our API constructor. We finally
call the method we want to use and retry.

.. code-block:: python

    from requests import Session
    from requests.adapters import HTTPAdapter, Retry

    from novu.api import EventApi

    session = Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
    session.mount("https://api.novu.co", HTTPAdapter(max_retries=retries))

    event_api = EventApi("https://api.novu.co", "<NOVU_API_TOKEN>", session=session)
    event_api.trigger(
        name="<YOUR_TEMPLATE_NAME>",
        recipients="<YOUR_SUBSCRIBER_ID>",
        payload={},  # Your Novu payload goes here
    )
