from slackclient import SlackClient
import io
import os

slack_client = SlackClient(os.environ.get('SLACK_API_TOKEN'))
r = slack_client.api_call("files.upload", filename='3D Printers.jpg', channels='#webcams',
    file=io.BytesIO(open('image.jpg','r').read())
    )
image_id = r['file']['id']

with open('uploaded.txt', 'a') as f:
    f.write(image_id + '\n')

