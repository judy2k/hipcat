# Hip Cat

Pipe things to HipChat from the command-line!

## Installation

You will need a working installation of [Python]() and [PIP]().

```bash
pip install hipcat
```

Go to [https://fanduel.hipchat.com/account/api](https://fanduel.hipchat.com/account/api) and create a new token. It only needs the 'Send Notification' scope, but this may change in future.

Create a file at `~/.hipcat.ini` that looks a bit like this:

```ini
[hipcat]
access_key = <put-your-token here>
```

# Using hipcat

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
