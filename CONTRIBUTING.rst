Contribution Guideline
======================

This part of the documentation is intended to show you how you can contribute to the project
without the risk of seeing your first modification proposals rejected by the project maintainers.

Coding Styles
-------------

- 4 spaces indentation
- Follow ``pylama.ini``
- Follow black formatting
- Methods and functions should be documented with `google python style guide <https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`_
- Methods and functions should be typed

Name Conventions
----------------

- Python: snake_case (Underscore)

Tools
-----

Make sure you got all these tools to start:

- Poetry >= 1.3
- Git
- IDE that supports `pyproject.toml` (I am using VS Code)

Install Dependencies for Development
------------------------------------

.. code-block:: shell

    poetry install
    poetry run pre-commit install --install-hook
    poetry run pre-commit install --install-hooks --hook-type commit-msg

Unit Test
---------

As part of the project, the 100% code coverage rule was put in place to force you to prove the
usefulness of the code you write. Here, 100% coverage does not mean that you will cover 100% of
the functionality with your tests, but that 100% of your code is functional within the interpreter.

This is a first step, but let's not stop here, the goal of the application unit tests is, each time
you develop a feature, to save its behavior in a scenario that will allow the next developer to understand
and ensure that these scenarios will thrive and not be altered by their modifications.

Take the time to understand the unit tests and the different tools that are put at your service by python
through the unittest and mock packages.

If you don't know anything about unit testing, here are some sources to learn:

* https://realpython.com/python-testing/

Linting
-------

Strict linting rules are put in place on the project such as This is for a very specific purpose:
we don't want the codes developed by one person to be marked with a signature.

Why is this? The idea behind the linting rules and automatic formatting is that every developer
follows the same development standards as the others so that the code can be written and reviewed much faster.

Not familiar with these tools yet? Try them for a while, you will see that by following their
recommendations you will become much more efficient, and especially that you will be able to concentrate
on the "useful" parts of the development rather than understanding what your peers wanted to write.

And if you're worried about it being a SpikeeLabs fad, these standards are applied worldwide.
Take a look here, everything will be explained much better than here: https://peps.python.org/pep-0008/

For those who continue to struggle with pylama, here is a little sweet to pass your pain: https://www.youtube.com/watch?v=hgI0p1zf31k

Dependencies
------------

All the management of installation and development dependencies is done through the poetry utility: https://python-poetry.org/

Most common action with this tool (in this project) are:

- Add a dev dependency using ``poetry add --group=dev <package_name>``
- Add a production dependency using ``poetry add <package_name>```
- Update a dependency using ``poetry update <package>``

.. warning:: You should never use the ``poetry update`` command without knowing what you are doing.
             This command causes all dependencies to be updated and often comes with a long bug-fixing
             time because your application no longer works.

             If you have inadvertently performed this command, you can always undo the changes that were
             applied to the poetry.lock file via the following commands:

             .. code-block:: shell

                git checkout -- poetry.lock
                poetry install

            If poetry is asking you to update the lock, don't run ``poetry lock`` to fulfill your duty but
            ``poetry lock --no-update`` instead.

Commit convention
-----------------

We are using `conventional commits <https://www.conventionalcommits.org/en/v1.0.0/>`_.

Here are the types used:

* feat: new features
* fix: bug fixes
* build: build system changes (poetry config)
* ci: CI script and config changes (github workflows)
* docs: Documentation update without other changes
* perf: Performance improvements
* refactor: Changes in code without feature change
* revert: For commit reverts
* style: Changes that do not change the meaning of code (whitespace)
* test: Adding tests or fixing tests, without changing the features or bugfix
* chore: Updates and releases

All commits in the ``alpha`` branch should follow this convention in order to have nice changelogs.

When a commit introduces a breaking change, add an annotation in the commit's footer, as follows:

.. code-block:: text

    type(scope): this has changed

    It changed because ...

    BREAKING CHANGE: this feature does not work as previously

What are the main branches used?
--------------------------------

There are two branches for deployments:

* ``main``: The production branch, every commit on it will be in the production release.
* ``alpha``: The development and integration branch. Every commit on it will go to the integration build and alpha releases.

When hotfix are added to ``main``, ``alpha`` should be rebased on ``main``.

Work is done in ``feat/`` and ``fix/`` branches. These are based on ``alpha``, and rebased on it before merge.

When merging a feature branch, care should be taken to only merge meaningful commits, in order to have a clean changelog.
The target is 1 commit = 1 changelog line = 1 meaningful change.
Squashing and commit reordering using an interactive rebase can help with this goal.

The hotfix branches work the same way, but are based on ``main``.
