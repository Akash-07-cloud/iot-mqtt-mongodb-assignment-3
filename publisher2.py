import paho.mqtt.client as mqtt
import json
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.loop_start()

with open("dataset.json") as file:
    data = json.load(file)

try:
    while True:
        for entry in data:
            if entry["device_type"] == "room":
                print(f"[Publisher2] → {entry}")
                client.publish("devices/room", json.dumps(entry), qos=1)
                time.sleep(2)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    print("Publisher2 stopped.")
