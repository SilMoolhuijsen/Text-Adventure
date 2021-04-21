import time
import os
import sys
txtSpeed5 = ["Very Fast", "very fast", "very Fast", "Very fast", "5"]
txtSpeed4 = ["Fast", "fast", "4"]
txtSpeed3 = ["Normal", "normal", "3"]
txtSpeed2 = ["Slow", "slow", "2"]
txtSpeed1 = ["Very Slow", "very slow", "very Slow", "Very slow", "1"]
PEQ = [".", "!", "?"]
COMMA = [","]

def choose_ts():
  ts = 0.005
  def slowprint(s):
    for letter in s:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(ts)

  TextSpeed = slowprint("Choose a text speed, Very Slow (1), Slow (2), Normal (3), Fast (4) or Very Fast (5): ")
  TextSpeed = input()
  if TextSpeed in txtSpeed5:
    ts = 0.005
  elif TextSpeed in txtSpeed4:
    ts = 0.01
  elif TextSpeed in txtSpeed3:
    ts = 0.02
  elif TextSpeed in txtSpeed2:
    ts = 0.05
  elif TextSpeed in txtSpeed1:
    ts = 0.1
  else:
    print("That is not a valid text speed. You can only choose Very Slow (1), Slow (2), Normal (3), Fast (4) or Very Fast (5).")
    choose_ts()

  def start():
    slowprint("What's your name?\n")
    user_name = input()
    slowprint("Okay " + user_name)
    slowprint(", let's embark on an adventure!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    intro()
  
  def intro():
    slowprint("Hello there.")

  start()

choose_ts()