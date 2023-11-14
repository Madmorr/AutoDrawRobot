import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import paho.mqtt.client as mqtt
from adafruit_motorkit import MotorKit


kit = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)


client = mqtt.Client()
client.connect("localhost", 1883, 60)  # Replace BROKER_IP with your broker's IP address

steps=300

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
    else:
        print(f"Connection failed with error code {rc}")
    client.subscribe("robot/control")

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))


def on_message(client, userdata, msg):
    command = msg.payload.decode()
    # Assuming commands like "forward", "backward", etc.
    if command == "forward":
        move_forward()
    elif command == "backward":
        move_backwards()
    elif command == "right":
        move_right()
    elif command == "left":
        move_left()    


client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect


def move_forward():
    for _ in range(steps):
        kit.stepper1.onestep(style=stepper.DOUBLE)
        kit.stepper2.onestep(style=stepper.DOUBLE)
        kit2.stepper1.onestep(style=stepper.DOUBLE)
        kit2.stepper2.onestep(style=stepper.DOUBLE)
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()

def move_backwards():
    for _ in range(steps):
        kit.stepper1.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
        kit.stepper2.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
        kit2.stepper1.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
        kit2.stepper2.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()

def move_right():
    for _ in range(steps):
        kit.stepper1.onestep(style=stepper.DOUBLE)
        kit.stepper2.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
        kit2.stepper1.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
        kit2.stepper2.onestep(style=stepper.DOUBLE)
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()

def move_left():
    for _ in range(steps):
        kit.stepper1.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
        kit.stepper2.onestep(style=stepper.DOUBLE)
        kit2.stepper1.onestep(style=stepper.DOUBLE)
        kit2.stepper2.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()



client.loop_forever()




