# HipCat

Pipe things to HipChat from the command-line!

Inspired by [Slackcat](https://github.com/rlister/slackcat)!

## Installation

You will need a working installation of [Python](https://www.python.org/) (you already have this if you're on Linux or OSX) and [PIP](https://pip.pypa.io/en/stable/installing/).

```bash
pip install hipcat
```

Go to [https://fanduel.hipchat.com/account/api](https://fanduel.hipchat.com/account/api) and create a new token. It only needs the 'Send Notification' scope, but this may change in future.

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

You want to contribute?? Love you!

There's some stuff you should know:

* Don't backport it to Python 2. Yes, I know it's easy. We should all be writing Python 3 now.
* Please treat me and any other contributors and commenters with respect.
* Please ensure that any changes follow PEP-8.
* When I add tests (there aren't any yet!) I plan to use tox and py.test. If you want to add tests, let's talk about it first.

## To Do

* Add `--quote` option for pre-pending the message with `/quote`
* Add a `--code` option for pre-pending the message with `/code`
* Errrrrr... post a GitHub issue if you want to see a new feature, and we'll talk!
