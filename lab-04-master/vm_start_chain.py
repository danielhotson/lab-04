"""EE 250L Lab 04 Start Chain Code"""

import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    client.subscribe("dhotson/pong")
    client.message_callback_add("dhotson/pong", on_message_from_pong)

def on_message_from_pong(client, userdata, message):
    print("Custom callback  - Pong: " + message.payload.decode())
    temp = int(message.payload.decode()) + 1
    time.sleep(1)
    client.publish("dhotson/ping", f"{temp}")
    print("Publishing ping")
    time.sleep(4)
   

    

if __name__ == '__main__':
    #get ping
    i = 0
    
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
  
    #connect to the RPI broker
    client.connect( host="192.168.133.4", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)
    client.publish("dhotson/ping", f"{i}")
    print("Publishing ping")

    while True:
        #replace user with your USC username in all subscriptions
        time.sleep(4)
