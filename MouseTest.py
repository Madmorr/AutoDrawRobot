import mouse
import time

while True:
    position = [0, 0]
    position = mouse.get_position()
    print("(" + str(position[0]) + ", " + str(position[1]) + ")")
    if (position[0] == 639):
        mouse.move(320, position[1])
    if (position[1] == 479):
        mouse.move(position[0], 240)
    if (position[0] == 0):
        mouse.move(320, position[1])
    if (position[1] == 0):
        mouse.move(position[0], 240)
    time.sleep(0.1)