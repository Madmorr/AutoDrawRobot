import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from sshkeyboard import listen_keyboard

kit = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)

steps=400


def move_forward():
    for _ in range(steps):
        kit.stepper1.onestep(style=stepper.INTERLEAVE)
        kit.stepper2.onestep(style=stepper.INTERLEAVE)
        kit2.stepper1.onestep(style=stepper.INTERLEAVE)
        kit2.stepper2.onestep(style=stepper.INTERLEAVE)
        #time.sleep(0.01)
 
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()

def move_backwards():
    for _ in range(steps):
        kit.stepper1.onestep(style=stepper.INTERLEAVE, direction=stepper.BACKWARD)
        kit.stepper2.onestep(style=stepper.INTERLEAVE, direction=stepper.BACKWARD)
        kit2.stepper1.onestep(style=stepper.INTERLEAVE, direction=stepper.BACKWARD)
        kit2.stepper2.onestep(style=stepper.INTERLEAVE, direction=stepper.BACKWARD)
        #time.sleep(0.01)  
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()

def move_right():
    for _ in range(steps):
        kit.stepper1.onestep(style=stepper.INTERLEAVE)
        kit.stepper2.onestep(style=stepper.INTERLEAVE, direction=stepper.BACKWARD)
        kit2.stepper1.onestep(style=stepper.INTERLEAVE, direction=stepper.BACKWARD)
        kit2.stepper2.onestep(style=stepper.INTERLEAVE)
        #time.sleep(0.01)
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()

def move_left():
    for _ in range(steps):
        kit.stepper1.onestep(style=stepper.INTERLEAVE, direction=stepper.BACKWARD)
        kit.stepper2.onestep(style=stepper.INTERLEAVE)
        kit2.stepper1.onestep(style=stepper.INTERLEAVE)
        kit2.stepper2.onestep(style=stepper.INTERLEAVE, direction=stepper.BACKWARD)
        #time.sleep(0.01)
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()

#releasing doesnt seem to actually release the motors//
def quit():
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()
    

def perform_operation(key):
    actions = {
        "up": move_forward,
        "w": move_forward,
        "left": move_left,
        "a": move_left,
        "down": move_backwards,
        "s": move_backwards,
        "right": move_right,
        "d": move_right,
        "esc": quit,
    }
    chosen_function = actions.get(key)
    chosen_function()

def press(key):
    perform_operation(key)
    
listen_keyboard(
    on_press=press,
    delay_second_char=0.01,
    delay_other_chars=0.01,
)








