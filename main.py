TextSpeed = input("Enter your preferred text speed (slow, normal or fast): ")
while TextSpeed <= 3 and TextSpeed > 0:
  if TextSpeed = "slow":
    txtspeed = 0.55
  elif TextSpeed = "normal":
    txtspeed = 0.4
  elif TextSpeed = "fast":
    txtspeed = 0.25
else:
print("This text speed is not valid, please enter fast, normal or slow\n")
 
import sys
import time
def slowprint(s):
  for letter in s:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(txtspeed)

slowprint("What's your name?\n")
user_name = input()
slowprint("Okay " + user_name)
time.sleep(0.2)
slowprint(", let's embark on an adventure!\n")
time.sleep(1)
import os
os.system('cls' if os.name == 'nt' else "printf '\033c'")
