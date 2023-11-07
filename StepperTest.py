import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)

for i in range(100):
    kit.stepper1.onestep(style=stepper.SINGLE)
    kit.stepper2.onestep(style=stepper.SINGLE)
    kit2.stepper1.onestep(style=stepper.SINGLE)
    kit2.stepper2.onestep(style=stepper.SINGLE)
    

time.sleep(1)

for i in range(100):
    kit.stepper1.onestep(style=stepper.DOUBLE)
    kit.stepper2.onestep(style=stepper.DOUBLE)
    kit2.stepper1.onestep(style=stepper.DOUBLE)
    kit2.stepper2.onestep(style=stepper.DOUBLE)
    

time.sleep(1)

for i in range(100):
    kit.stepper1.onestep(style=stepper.INTERLEAVE)
    kit.stepper2.onestep(style=stepper.INTERLEAVE)
    kit2.stepper1.onestep(style=stepper.INTERLEAVE)
    kit2.stepper2.onestep(style=stepper.INTERLEAVE)
    

time.sleep(1)

for i in range(100):
    kit.stepper1.onestep(style=stepper.MICROSTEP)
    kit.stepper2.onestep(style=stepper.MICROSTEP)
    kit2.stepper1.onestep(style=stepper.MICROSTEP)
    kit2.stepper2.onestep(style=stepper.MICROSTEP)
    

kit.stepper1.release()
kit.stepper2.release()
kit2.stepper1.release()
kit2.stepper2.release()
