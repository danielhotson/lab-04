"""EE 250L Lab 04 Cont Chain Code"""

import paho.mqtt.client as mqtt
import time

global temp

def on_connect(client, userdata, flags, rc):
    client.subscribe("dhotson/ping")
    client.message_callback_add("dhotson/ping", on_message_from_ping)

def on_message_from_ping(client, userdata, message):
    print("Custom callback  - Ping: "+message.payload.decode())
    temp = int(message.payload.decode()) + 1
    time.sleep(1)
    client.publish("dhotson/pong", f"{temp}")
    print("Publishing pong")
    time.sleep(4)
    

if __name__ == '__main__':
    #get pong
    
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
  
    #connect to the RPI broker
    client.connect(host="192.168.133.4", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)

    while True:
        #replace user with your USC username in all subscriptions
        time.sleep(4)
