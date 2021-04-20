import time
import os
import sys

def ChooseTextSpeed():
  def slowprint(s):
    for letter in s:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(txtSpeed)

  TextSpeed = input("Choose a text speed, Slow (1), Normal (2) or Fast (3): ")  
  if TextSpeed in "Fast" or "fast" or "3":
    txtSpeed = 0.025
  elif TextSpeed in "Normal" or "normal" or "2":
    txtSpeed = 0.075
  elif TextSpeed in "Slow" or "slow" or "1":
    txtSpeed = 0.0125
  else:
    print("That is not a valid text speed. Choose from slow, normal or fast.")
    time.sleep(0.8)
    ChooseTextSpeed()

  def start():
    slowprint("What's your name?\n")
    user_name = input()
    slowprint("Okay " + user_name)
    time.sleep(0.2)
    slowprint(", let's embark on an adventure!\n")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
  start()

ChooseTextSpeed()