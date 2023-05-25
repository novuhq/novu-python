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
