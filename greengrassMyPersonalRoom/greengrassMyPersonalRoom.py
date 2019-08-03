#
# Triggered by message to rooms/requested
#

import greengrasssdk
import platform
import time
import json
import subprocess

# Creating a greengrass core sdk client
client = greengrasssdk.client('iot-data')

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()


def function_handler(event, context):
    global userId
    userId = event["userId"]
    if not my_platform:
        client.publish(
            topic='rooms/accepted',
            payload=json.dumps({'message': 'Person accepted. userId: {}'.format(userId), 'event': ''.format(event), 'context': ''.format(context)})
        )
    else:
        client.publish(
            topic='rooms/accepted',
            payload=json.dumps({'message': 'Person accepted. userId: {}. Platform: {}. '
                                .format(userId, my_platform), 'event': '{}'.format(event), 'context': '{}'.format(context)})
        )
    time.sleep(1)
    subprocess.call("chromium-browser https://www.entra.no", shell=True)
    # chromium-browser www.youtube.com -start-fullscreen &; pid=$!; sleep 1m; kill -15 $pid <- for later use
    return