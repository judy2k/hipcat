# HipCat

Pipe things to HipChat from the command-line!

Inspired by [Slackcat](https://github.com/rlister/slackcat)!


## Installation

You will need a working installation of [Python 3](https://www.python.org/)
(you probably already have this if you're on Linux or OSX) and
[PIP](https://pip.pypa.io/en/stable/installing/).

```bash
pip install hipcat
```

Go to [https://www.hipchat.com/account/api](https://www.hipchat.com/account/api)
and create a new token. It only needs the 'Send Notification' scope, but this
may change in future.

Create a file at `~/.hipcat.ini` that looks a bit like this:

```ini
[hipcat]
access_token = <put-your-token here>
```


## Using hipcat

You can get help by running `hipcat --help`, but the basics look like this:

```bash
# Pipe output from one command to HipChat:
echo 'This is my message' | hipcat 'Room Name'
```

If you don't want to pass the message via a pipe, you can instead provide
it as a parameter:

```bash
# Run a long running command and then notify on HipChat
my-long-task && hipcat 'Notifications' -m "The long-running task is done"
```


## Contributing to hipcat

You want to contribute? Love you!

There's some stuff you should know:

* **Please don't** backport it to Python 2. Yes, I know it's easy. We should
  all be writing Python 3 now.
* Please treat other contributors and commenters with respect.
* Please ensure that any changes follow PEP-8.
* When I add tests (there aren't any yet!) I plan to use py.test. If
  you want to help by addind tests, let's talk about it first.


## To Do

* Add `--quote` option for pre-pending the message with `/quote`
* Add a `--code` option for pre-pending the message with `/code`
* Add a flag to send the output to HipChat line-by-line rather than at the end.
* Err... post a GitHub issue if you want to see a new feature, and we'll talk!
