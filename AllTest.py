import time
import board
import math
import smbus
from sshkeyboard import listen_keyboard
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)

class PCA9685:
  __SUBADR1            = 0x02
  __SUBADR2            = 0x03
  __SUBADR3            = 0x04
  __MODE1              = 0x00
  __PRESCALE           = 0xFE
  __LED0_ON_L          = 0x06
  __LED0_ON_H          = 0x07
  __LED0_OFF_L         = 0x08
  __LED0_OFF_H         = 0x09
  __ALLLED_ON_L        = 0xFA
  __ALLLED_ON_H        = 0xFB
  __ALLLED_OFF_L       = 0xFC
  __ALLLED_OFF_H       = 0xFD

def __init__(self, address=0x40, debug=False):
    self.bus = smbus.SMBus(1)
    self.address = address
    self.debug = debug
    if (self.debug):
        print("Reseting PCA9685")
    self.write(self.__MODE1, 0x00)
	
def write(self, reg, value):
    "Writes an 8-bit value to the specified register/address"
    self.bus.write_byte_data(self.address, reg, value)
    if (self.debug):
        print("I2C: Write 0x%02X to register 0x%02X" % (value, reg))
	  
def read(self, reg):
    "Read an unsigned byte from the I2C device"
    result = self.bus.read_byte_data(self.address, reg)
    if (self.debug):
        print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" % (self.address, result & 0xFF, reg))
    return result
	
def setPWMFreq(self, freq):
    "Sets the PWM frequency"
    prescaleval = 25000000.0    # 25MHz
    prescaleval /= 4096.0       # 12-bit
    prescaleval /= float(freq)
    prescaleval -= 1.0
    if (self.debug):
        print("Setting PWM frequency to %d Hz" % freq)
        print("Estimated pre-scale: %d" % prescaleval)
    prescale = math.floor(prescaleval + 0.5)
    if (self.debug):
        print("Final pre-scale: %d" % prescale)

    oldmode = self.read(self.__MODE1);
    newmode = (oldmode & 0x7F) | 0x10        # sleep
    self.write(self.__MODE1, newmode)        # go to sleep
    self.write(self.__PRESCALE, int(math.floor(prescale)))
    self.write(self.__MODE1, oldmode)
    time.sleep(0.005)
    self.write(self.__MODE1, oldmode | 0x80)

def setPWM(self, channel, on, off):
    "Sets a single PWM channel"
    self.write(self.__LED0_ON_L+4*channel, on & 0xFF)
    self.write(self.__LED0_ON_H+4*channel, on >> 8)
    self.write(self.__LED0_OFF_L+4*channel, off & 0xFF)
    self.write(self.__LED0_OFF_H+4*channel, off >> 8)
    if (self.debug):
        print("channel: %d  LED_ON: %d LED_OFF: %d" % (channel,on,off))
	  
def setServoPulse(self, channel, pulse):
    "Sets the Servo Pulse,The PWM frequency must be 50HZ"
    pulse = pulse*4096/20000        #PWM frequency is 50HZ,the period is 20000us
    self.setPWM(channel, 0, int(pulse))

def move_servo_90():
    pwm = PCA9685()
    pwm.setPWMFreq(50)
    for i in range(500,2500,10):
      pwm.setServoPulse(0,i) 
      time.sleep(0.02) 

def move_servo_90_negative():
    pwm = PCA9685()
    pwm.setPWMFreq(50)
    for i in range(2500,500,-10):
      pwm.setServoPulse(0,i) 
      time.sleep(0.02) 

def move_forward():
    kit.stepper1.onestep()
    kit.stepper2.onestep()
    kit2.stepper1.onestep()
    kit2.stepper2.onestep()

def move_backwards():
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit2.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep(direction=stepper.BACKWARD)

def move_left():
    kit.stepper1.onestep()
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit2.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep()

def move_right():
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep()
    kit2.stepper1.onestep()
    kit2.stepper2.onestep(direction=stepper.BACKWARD)

def diagonal_up_left():
    kit.stepper2.onestep()
    kit2.stepper1.onestep()

def diagonal_up_right():
    kit.stepper1.onestep()
    kit2.stepper2.onestep()

def diagonal_down_left():
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit2.stepper1.onestep(direction=stepper.BACKWARD)

def diagonal_down_right():
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep(direction=stepper.BACKWARD)

def rotate_center_clockwise():
    kit.stepper1.onestep()
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit2.stepper1.onestep()
    kit2.stepper2.onestep(direction=stepper.BACKWARD)

def rotate_center_counterclockwise():
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep()
    kit2.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep()

def rotate_corner_front_left():
    kit.stepper2.onestep()
    kit2.stepper2.onestep()

def rotate_corner_front_right():
    kit.stepper1.onestep()
    kit2.stepper1.onestep()

def rotate_corner_back_left():
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep(direction=stepper.BACKWARD)

def rotate_corner_back_right():
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper1.onestep(direction=stepper.BACKWARD)

def rotate_axis_front():
    kit2.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep()

def rotate_axis_back():
    kit.stepper1.onestep()
    kit.stepper2.onestep(direction=stepper.BACKWARD)
         
def quit():
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()
    exit()

def perform_operation(key):
    actions = {
        "o": move_servo_90,
        "p": move_servo_90_negative,
        "up": move_forward,
        "w": move_forward,
        "right": move_left,
        "d": move_left,
        "down": move_backwards,
        "s": move_backwards,
        "left": move_right,
        "a": move_right,
        "q": diagonal_up_left,
        "e": diagonal_up_right,
        "z": diagonal_down_left,
        "c": diagonal_down_right,
        "x": rotate_center_clockwise,
        "g": rotate_center_counterclockwise,
        "r": rotate_corner_front_left,
        "y": rotate_corner_front_right,
        "v": rotate_corner_back_left,
        "n": rotate_corner_back_right,
        "t": rotate_axis_front,
        "b": rotate_axis_back,
        "esc": quit,
    }
    chosen_function = actions.get(key, printkey(key))
    chosen_function()

def press(key):
    perform_operation(key)

def printkey(key):
    print("PRESSED", key)
    
listen_keyboard(
    on_press=press,
    delay_second_char=0.01,
    delay_other_chars=0.01,
)