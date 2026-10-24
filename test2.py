from datetime import datetime
import math
import sys

sys.set_int_max_str_digits(0)
now = datetime.now()

print(now.strftime("%I:%M %p"))     
print(now.strftime("%Y-%m-%d %H:%M:%S"))   
print(now.strftime("%A, %d %B %Y"))       

