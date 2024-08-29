#!/usr/bin/env python3

import os
import click

from toslack import Message
from toslack import Client

@click.group(invoke_without_command=False)
@click.option('--token', required=False, type=str, default='', help='slack robot token')
@click.option('--channel', required=False, type=str, default='', help='slack channel name')
@click.option('--channel-id', required=False, type=str, default='', help='slack channel ID')
@click.pass_context
def cli(ctx, token, channel, channel_id):

    ctx.obj = {}
    ctx.obj['token'] = os.environ.get('SLACK_TOKEN') if token == '' else token
    ctx.obj['channel'] = os.environ.get('SLACK_CHANNEL') if channel == '' else channel
    ctx.obj['channel_id'] = os.environ.get('SLACK_CHANNEL_ID') if channel_id == '' else channel_id

@cli.command()
@click.argument('arg')
@click.pass_context
def post(ctx, arg):
    client = Client(token=ctx.obj['token'], channel=ctx.obj['channel'])
    message = Message(client=client)
    message.post(text=arg)

@cli.command()
@click.argument('arg')
@click.pass_context
def upload(ctx, arg):    
    client = Client(token=ctx.obj['token'], channel_id=ctx.obj['channel_id'])
    message = Message(client=client)
    message.upload(file_path=arg)

if __name__ == '__main__':
    cli()