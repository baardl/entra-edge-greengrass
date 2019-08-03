#
# Triggered by message to rooms/requested
#

import greengrasssdk
import platform
import time
import json

# Creating a greengrass core sdk client
client = greengrasssdk.client('iot-data')

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()

# Counter to keep track of invocations of the function_handler
my_counter = 0


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
            payload=json.dumps({'message': 'Person accepted. userId: {}. Platform: {}.  Invocation Count: {}'
                                .format(userId, my_platform, my_counter), 'event': '{}'.format(event), 'context': '{}'.format(context)})
        )
    time.sleep(1)
    return