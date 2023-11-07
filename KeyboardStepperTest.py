import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from sshkeyboard import listen_keyboard

kit = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)

def move_forward():
    kit.stepper1.onestep()
    kit.stepper2.onestep()
    kit2.stepper1.onestep()
    kit2.stepper2.onestep()
    time.sleep(0.01)  

def move_backwards():
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit2.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep(direction=stepper.BACKWARD)
    time.sleep(0.01)  

def move_left():
    kit.stepper1.onestep()
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit2.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep()
    time.sleep(0.01)

def move_right():
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep()
    kit2.stepper1.onestep()
    kit2.stepper2.onestep(direction=stepper.BACKWARD)
    time.sleep(0.01)
         
def quit():
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()
    exit()

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
