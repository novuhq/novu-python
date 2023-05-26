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

How to take control over the session of ``requests``?
-----------------------------------------------------

Sometime, you may want to setup advanced usage involving the use of a ``requests`` :class:`~requests.Session`.

By default, a session is declared for every request you make to the API, but you can also
provide your own session and reuse it over and over again.

To illustrate this use case, let's take the example of setting up an automatic retry mechanism on
requests when the API responds with a 502, 503 or 504 HTTP codes.

To do this, before initializing the Event API, we'll first instantiate a :class:`~requests.Session` from the
:module:`requests` module, then we'ill inject it into the keywords arguments of our API constructor. We finally
call the method we want to use and retry.

.. code-block:: python

    from requests import Session
    from requests.adapters import HTTPAdapter, Retry

    from novu.api import EventApi

    session = Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
    session.mount("https://api.novu.co", HTTPAdapter(max_retries=retries))

    event_api = EventApi("https://api.novu.co/api/", "<NOVU_API_TOKEN>", session=session)
    event_api.trigger(
        name="<YOUR_TEMPLATE_NAME>",
        recipients="<YOUR_SUBSCRIBER_ID>",
        payload={},  # Your Novu payload goes here
    )
