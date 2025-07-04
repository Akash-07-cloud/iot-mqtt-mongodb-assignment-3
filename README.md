# IoT Assignment 3 – Patient Monitoring System (MQTT + Node-RED + MongoDB)

This project simulates a patient monitoring system that continuously publishes vitals (heart rate, blood pressure) and room temperature using MQTT. The data is received by Node-RED and stored in MongoDB.

## 🔧 Tools & Technologies
- Python (`paho-mqtt`) for simulation
- MQTT protocol (Mosquitto)
- Node-RED as MQTT subscriber and processor
- MongoDB Compass for real-time data storage

## 📁 Folder Contents

| File             | Description                             |
|------------------|-----------------------------------------|
| `dataset.json`   | Sample data used by publishers          |
| `publisher1.py`  | Publishes vitals data to MQTT broker    |
| `publisher2.py`  | Publishes room temperature to MQTT      |
| `flow.json`      | Exported Node-RED flow (optional)       |
| `README.md`      | Project documentation                   |

## 🔄 Flow Overview

1. `publisher1.py` and `publisher2.py` continuously send simulated sensor data via MQTT.
2. Node-RED receives the messages using `mqtt in` node.
3. Messages are routed based on `device_type` using a `switch` node.
4. Data is stored in:
   - `vitals-data` collection (heart rate, BP)
   - `room-temp-data` collection (room temperature)

## 🖼 Output Screenshots

- ✅ Node-RED debug output with structured payloads
- ✅ MongoDB Compass showing stored documents in two collections

## 🧠 Learning Outcomes

- Real-time MQTT communication
- IoT edge device simulation
- NoSQL data storage and querying
