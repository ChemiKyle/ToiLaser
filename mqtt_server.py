#!/usr/bin/env python3

from db_interface import  *
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with code: {}".format(str(rc)))
    # Here's a quick way to sub to multiple topics with one server
    # in case you wanted to do something actually useful
    topics = ["toilaser"]
    [client.subscribe(topic) for topic in topics]


def on_message(client, userdata, msg):
    print("message received")
    print(str(msg.payload.decode("utf-8")))
    location_id = int(msg.payload.decode("utf-8"))
    conn = create_connection()
    add_timestamp(conn, location_id)
    conn.close()


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
