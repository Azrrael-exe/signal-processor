import paho.mqtt.client as mqtt


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")


def on_message(client, userdata, message):
    print(f"Received message: {message.payload}")
    read = parse(message.payload)
    with open("output.txt", "a") as file:
        file.write(f"{read}\n")


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        client.subscribe("sda-iot-2024/vcamargo", 1)


def parse(data: bytes) -> dict:
    payload = data[2:-1]
    chunks = [payload[i : i + 3] for i in range(0, len(payload), 3)]
    return {hex(chunck[0]): (chunck[1] << 8 | chunck[2]) for chunck in chunks}


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe

mqttc.user_data_set([])
mqttc.connect("broker.hivemq.com")
mqttc.loop_forever()
