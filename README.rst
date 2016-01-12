HipCat
======

Pipe things to HipChat from the command-line!

Inspired by `Slackcat <https://github.com/rlister/slackcat>`__!

Installation
------------

You will need a working installation of `Python
3 <https://www.python.org/>`__ (you probably already have this if you're
on Linux or OSX) and
`PIP <https://pip.pypa.io/en/stable/installing/>`__.

.. code:: bash

    pip3 install hipcat

Go to https://www.hipchat.com/account/api and create a new token. It
only needs the 'Send Message' scope, but this may change in future.

Create a file at ``~/.hipcat.ini`` that looks a bit like this:

.. code:: ini

    [hipchat]
    access_token = <put-your-token here>

Using hipcat
------------

You can get help by running ``hipcat --help``, but the basics look like
this:

.. code:: bash

    # Pipe output from one command to HipChat:
    echo 'This is my message' | hipcat 'Room Name'

If you don't want to pass the message via a pipe, you can instead
provide it as a parameter:

.. code:: bash

    # Run a long running command and then notify on HipChat
    my-long-task && hipcat 'Notifications' -m "The long-running task is done"

If the text you are sending to HipChat is formatted, use the ``-q`` flag
to prefix with ``/quote``, and if it should be syntax-highlighted code,
use the ``-c`` flag to prefix with ``/code``.

Contributing to hipcat
----------------------

You want to contribute? Love you!

There's some stuff you should know:

-  **Please don't** backport it to Python 2. Yes, I know it's easy. We
   should all be writing Python 3 now.
-  Please treat other contributors and commenters with respect.
-  Please ensure that any changes follow PEP-8.
-  When I add tests (there aren't any yet!) I plan to use py.test. If
   you want to help by addind tests, let's talk about it first.

To Do
-----

-  Add a flag to send the output to HipChat line-by-line rather than at
   the end.
-  Allow message posting to individuals as well as rooms.
-  Allow uploading content as a file rather than inline text.
-  Err... post a GitHub issue if you want to see a new feature, and
   we'll talk!
