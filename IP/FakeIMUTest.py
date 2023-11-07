import time
import random

# conservative warm-up time
random.seed(time.time())
    
rand1 = random.uniform(2,7)
rand2 = random.uniform(2,7)
rand3 = random.uniform(2,7)
print("{:<15}".format("Gyro:   ") + "{:<15}".format("Aclr:   ") + "{:<15}".format("Mgnt:   "))

# Just call e.g. bmx.gyro to read the gyro value
for i in range(0,100,1):
    rand1 += random.uniform(-1,1)
    rand2 += random.uniform(-1,1)
    rand3 += random.uniform(-1,1)
    print("{:<15}".format(str(f'{rand1:<15.3f}')) + "{:<15}".format(str(f'{rand2:<15.3f}')) + "{:<15}".format(str(f'{rand3:<15.3f}')))
    time.sleep(0.1)