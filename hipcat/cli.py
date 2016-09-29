#!/usr/bin/env python3

"""
Pipe text to a HipChat room.
"""

import configparser
import json
import os
import sys

import click
import requests


APP_NAME = 'hipcat'


class UserError(Exception):
    pass


class ConfigurationError(UserError):
    pass


class Config(object):
    def load(self):
        config_paths = [
            os.path.expanduser('~/.hipcat.ini'),
            os.path.join(click.get_app_dir(APP_NAME), 'config.ini'),
            os.path.join(
                click.get_app_dir(APP_NAME, force_posix=True), 'config.ini'
            ),
        ]
        config = configparser.ConfigParser()
        configs_found = config.read(config_paths)
        if not configs_found:
            raise ConfigurationError("""
Missing configuration!

You must provide configuration in one of the following places:

""" + "\n".join(' * {}'.format(path) for path in config_paths) + """
"""
            )
        self.config = config

        return self

    @property
    def hipchat_token(self):
        token = self.config.get('hipchat', 'access_token', fallback=None)
        if not token:
            raise ConfigurationError(
"""
Configuration error!

You must provide an 'access_token' in your configuration's 'hipchat' section.
"""
            )
        return token

    @property
    def base_url(self):
        return self.config.get('hipchat', 'base_url', fallback='https://www.hipchat.com').rstrip('/')



@click.command(help=__doc__)
@click.version_option()
@click.argument('room')
@click.option('--notification', help='Whether the message should be sent as a notification instead.', is_flag=True)
@click.option('-m', '--message', help='A message to post. Uses STDIN if not provided.')
@click.option('-q', '--quote', help='Prefix the message with /quote for formatting.', is_flag=True)
@click.option('-c', '--code', help='Prefix the message with /code for formatting.', is_flag=True)
@click.option('-s', '--sender', help='A label to be shown in addition to the sender\'s name.')
@click.option('--color', help='Background color for message. Valid values: yellow, green, red, purple, gray, random.')
@click.option('-n', '--notify', help='Whether this message should trigger a user notification.', is_flag=True)
def main(room, notification, message, quote, code, sender, color, notify):
    try:
        config = Config().load()

        url = '{config.base_url}/v2/{user_or_room}/{room_id_or_name}/{endpoint}'.format(
            config=config,
            room_id_or_name=room,
            endpoint='notification' if notification else 'message',
            user_or_room='user' if room.startswith('@') else 'room'
        )
        print(url)

        message = message or sys.stdin.read()
        if message:
            if quote or code:
                message = '{formatter} {message}'.format(
                    formatter='/quote' if quote else '/code',
                    message=message
                )

            if color and color not in ('yellow', 'green', 'red', 'purple', 'gray', 'random'):
                print(
                    'Invalid value {color} for color. Valid values are: yellow, green, red, purple, gray, random.'.format(
                        color=color
                    ),
                    file=sys.stderr
                )
                exit(1)

            response = requests.post(
                url,
                headers={
                    'Authorization': 'Bearer {}'.format(config.hipchat_token),
                    'Content-Type': 'application/json',
                },
                data=json.dumps({
                    'message': message,
                    'notify': notify,
                    'from': sender or 'hipcat' if notify else '',
                    'color': color or 'yellow'
                }),
            )
            if response.status_code > 299:
                response = response.json()
                if 'error' in response:
                    print(response['error']['message'], file=sys.stderr)
                    exit(1)
    except KeyboardInterrupt:
        exit(1)
    except UserError as user_error:
        print(user_error, file=sys.stderr)
        exit(2)
