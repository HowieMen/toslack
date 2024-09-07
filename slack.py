import os
import click

from toslack import SlackMessage
from toslack import SlackClient

@click.group(invoke_without_command=False)
@click.option('--token', required=False, type=str, default='', help='slack robot token')
@click.option('--channel', required=False, type=str, default='', help='slack channel ID')
@click.pass_context
def cli(ctx, token, channel):

    ctx.obj = {}
    ctx.obj['token'] = os.environ.get('SLACK_BOT_TOKEN') if token == '' else token
    ctx.obj['channel'] = os.environ.get('TO_SLACK_CHANNEL') if channel == '' else channel

@cli.command()
@click.argument('arg')
@click.pass_context
def post(ctx, arg):
    client = SlackClient(token=ctx.obj['token'], channel=ctx.obj['channel'])
    message = SlackMessage(client=client)
    message.post(text=arg)

@cli.command()
@click.argument('arg')
@click.pass_context
def upload(ctx, arg):    
    client = SlackClient(token=ctx.obj['token'], channel=ctx.obj['channel'])
    message = SlackMessage(client=client)
    message.upload(file_path=arg)

if __name__ == '__main__':
    cli()