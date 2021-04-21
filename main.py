import time
import os
import sys
period = 0.8
comma = 0.2
txtSpeed3 = ["Fast", "fast", "3"]
txtSpeed2 = ["Normal", "normal", "2"]
txtSpeed1 = ["Slow", "slow", "1"]

def start_game():
  TextSpeed = input("Choose a text speed, Slow (1), Normal (2) or Fast (3): ")
  if TextSpeed in txtSpeed3:
    ts = 0.02
  elif TextSpeed in txtSpeed2:
    ts = 0.04
  elif TextSpeed in txtSpeed1:
    ts = 0.1
  else:
    print("That is not a valid text speed. You can only choose slow (1), normal (2) or fast (3).")
    time.sleep(period)
    start_game()

  def slowprint(s):
    for letter in s:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(ts)
  
  slowprint("What's your name?\n")
  user_name = input()
  slowprint("Okay " + user_name)
  time.sleep(comma)
  slowprint(", let's embark on an adventure!\n")
  time.sleep(1)
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  start()
start_game()

def start():
  print("Hello there.")
  time.sleep(period)