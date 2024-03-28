# Import required libraries
import random
import paho.mqtt.publish as publish

# MQTT Broker Information for ThingSpeak
mqttHost = "mqtt3.thingspeak.com"

# Environment Station ID
topic1 = "channels/2483692/publish"
topic2 = "channels/2486803/publish"

# Unique MQTT ID for the environmental station
client_ID = ["BBE8NAghARASLxQlJBUiHzc", "CAIOHTABES4pGTQmBx8EGDA"]
username = ["BBE8NAghARASLxQlJBUiHzc", "CAIOHTABES4pGTQmBx8EGDA"]
password = ["v5mKtA5ggwuZkEOwHuX9pigI", "mOgNupK4o9UibJsXESIKzICg"]

# Communication parameters
transport = "websockets"
port = 80


try:
    while True:
        # Generate random sensor values
        temperature = round(random.uniform(-50, 50), 2)  # Range: -50 to 50 Celsius
        humidity = round(random.uniform(0, 100), 2)     # Range: 0 to 100%
        co2 = round(random.uniform(300, 2000), 2)       # Range: 300ppm to 2000ppm
        
        # Generate Payload
        payload = f"field1={temperature}&field2={humidity}&field3={co2}"
        print(payload)

        # Publish Payload to Station 1
        publish.single(topic1, payload, hostname=mqttHost, transport=transport, port=port, client_id=client_ID[0], auth={'username':username[0],'password':password[0]})
        print(f"Published Device 1: {payload}")
        
        # Generate random sensor values
        temperature = round(random.uniform(-50, 50), 2)  # Range: -50 to 50 Celsius
        humidity = round(random.uniform(0, 100), 2)     # Range: 0 to 100%
        co2 = round(random.uniform(300, 2000), 2)       # Range: 300ppm to 2000ppm
        
        # Generate Payload
        print(payload)

        # Publish Payload to Station 2
        publish.single(topic2, payload, hostname=mqttHost, transport=transport, port=port, client_id=client_ID[1], auth={'username':username[1],'password':password[1]})
        print(f"Published Device 2: {payload}")
        
# Catch any errors
except KeyboardInterrupt:
    print("Exiting program")

except Exception as e:
        print (e)
