#!/usr/bin/env python3

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with code: {}".format(str(rc)))
    topics = ["toilaser"]
    [client.subscribe(topic) for topic in topics]


def on_message(client, userdata, msg):
    print("message received")
    print(str(msg.payload))
    # TODO: log to database


def mqtt_init():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.loop_forever()
    return(client)


def main():
    client = mqtt_init()
    if KeyboardInterrupt:
        client.disconnect()
        client.loop_stop()


if __name__ == '__main__':
    main()
