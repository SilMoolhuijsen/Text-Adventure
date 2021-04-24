import time
import os
import sys

txtSpeed5 = ["Very Fast", "very fast", "very Fast", "Very fast", "5"]
txtSpeed4 = ["Fast", "fast", "4"]
txtSpeed3 = ["Normal", "normal", "3"]
txtSpeed2 = ["Slow", "slow", "2"]
txtSpeed1 = ["Very Slow", "very slow", "very Slow", "Very slow", "1"]

def start_game():
  ts = 0.0075
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
    start_game()
  
  PERIOD = ts * 8
  COMMA = ts * 4

  def start():
    slowprint("What's your name?\n")
    user_name = input()
    slowprint("Okay " + user_name + ",")
    time.sleep(COMMA)
    slowprint(" let's embark on an adventure!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    intro()

  def intro():
    slowprint("You're a millionair and retired CIA agent.")
    time.sleep(PERIOD)
    slowprint(" You were one of the best fighters of the entire CIA.")
    time.sleep(PERIOD)
    slowprint(" But you're not as skillfull as you were 25 years ago.")
    time.sleep(PERIOD)
    slowprint(" You're 55 years old now.")
    time.sleep(PERIOD)
    slowprint(" It's been 3 years since you retired.")
    time.sleep(PERIOD)
    slowprint(" You've just been enjoying life since then.")
    time.sleep(PERIOD)
    slowprint(" But that is all going to change.\n\n")
    input("Press Enter")
    slowprint("\nOne morning,")
    time.sleep(COMMA)
    slowprint(" you wake up.")
    time.sleep(PERIOD)
    slowprint(" For some reason,")
    time.sleep(COMMA)
    slowprint(" you're sitting in a chair.")
    time.sleep(PERIOD)
    slowprint(" When you analyse the situation,")
    time.sleep(COMMA)
    slowprint(" you notice you don't know this place.")
    time.sleep(PERIOD)
    slowprint(" Now,")
    time.sleep(COMMA)
    slowprint(" you also feel your ankles and torso have been tied to the chair.")
    time.sleep(PERIOD)
    slowprint(" You don't know how or why you're here.")
    time.sleep(PERIOD)
    slowprint(" But you know you have to get out here immediately.\n")
    time.sleep(PERIOD)
    input("Press Enter")
    slowprint("\n")
  start()
  

start_game()