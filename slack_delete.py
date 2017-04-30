from slackclient import SlackClient
import io
import os

slack_client = SlackClient(os.environ.get('SLACK_API_TOKEN'))

for uploaded in open('uploaded.txt', 'r').readlines():
    slack_client.api_call("files.delete", file=uploaded.strip())

open('uploaded.txt', 'w')
