# HipCat

Pipe things to HipChat from the command-line!

Inspired by [Slackcat](https://github.com/rlister/slackcat)!


## Installation

You will need a working installation of [Python 3](https://www.python.org/)
(you probably already have this if you're on Linux or OSX) and
[PIP](https://pip.pypa.io/en/stable/installing/).

```bash
pip3 install hipcat
```

Go to [https://www.hipchat.com/account/api](https://www.hipchat.com/account/api)
and create a new token. It only needs the 'Send Message' scope, but this
may change in future.

Create a file at `~/.hipcat.ini` that looks a bit like this:

```ini
[hipchat]
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

If the text you are sending to HipChat is formatted, use the `-q` flag to
prefix with `/quote`, and if it should be syntax-highlighted code, use the
`-c` flag to prefix with `/code`.

You can send a direct message by using the 'mention name' of a user instead of
a room name:

```bash
echo "You are great" | hipcat '@FriendlyDave'

## Notifications

The message you are sending may also be treated as a [room
notification](<https://www.hipchat.com/docs/apiv2/method/send_room_notification>)
via the `--notification` flag. The following additional options and
flags are then recognized by hipcat:

- `--color` to specify background color for the message. Valid values:
yellow, green, red, purple, gray, random. Defaults to *yellow*.
- `--sender` to specify a label to be shown in addition to the sender's
name. Defaults to *hipcat* if `--notify` (see below) is specified as
well.
- `--notify` to ensure this message triggers a user notification.

```bash
# Send a message "Message" with a purple background, from "BOT" and with a
# user notification:
hipcat 'Notifications' --notification --notify -m "Message" --color=purple --sender="BOT"
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

* Add a flag to send the output to HipChat line-by-line rather than at the end.
* Allow message posting to individuals as well as rooms.
* Allow uploading content as a file rather than inline text.
* Err... post a GitHub issue if you want to see a new feature, and we'll talk!
