import time
import os
import sys

txtSpeed5 = ["Very Fast", "very fast", "very Fast", "Very fast", "5"]
txtSpeed4 = ["Fast", "fast", "4"]
txtSpeed3 = ["Normal", "normal", "3"]
txtSpeed2 = ["Slow", "slow", "2"]
txtSpeed1 = ["Very Slow", "very slow", "very Slow", "Very slow", "1"]
END_SENTENCE = [".", "!", "?"]
COMMA = ","

def start_game():
  ts = 0.0075
  def slowprint(s):
    for letter in s:
      sys.stdout.write(letter)
      sys.stdout.flush()
      if letter in COMMA:
        time.sleep(ts * 8)
      if letter in END_SENTENCE:
        time.sleep(ts * 16)
      else:
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
    slowprint("\nThat is not a valid text speed. You can only choose Very Slow (1), Slow (2), Normal (3), Fast (4) or Very Fast (5).\n\n")
    time.sleep(0.5)
    start_game()
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

  def start():
    slowprint("What's your name?\n")
    user_name = input()
    slowprint("\nOkay " + user_name + ", let's embark on an adventure!")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    time.sleep(1)
    intro()

  def intro():
    slowprint("You're a millionair and retired CIA agent. You were one of the best fighters ofas the entire CIA. But you're not as skillfull as you were 25 years ago. You're 55 years old now. It's been 3 years since you retired. You've just been enjoying life since then. But that is all going to change.\n\n")
    input("Press Enter")
    slowprint("\nOne morning, you wake up. When you analyse the situation, you notice that you're not in your bed, you're sitting in a chair. Also, you don't know this place. It's a room with no windows. Now, you also feel your ankles and torso have been tied to the chair that you're sitting in. You hear deep voices talking in the background. Maybe they're criminals who kidnapped you for your money. Or perhaps they want classified information about the CIA. You have no idea how or why you're in this situation. But you know that you have to get out of here as soon as possible.\n\n")
    input("Press Enter")
    slowprint("\nYou don't feel any weapons on you, so you start to examine the room.\n")
    slowprint("You find you're sitting exactly in the centre of the room.\n")
    slowprint("You see a machete on the table against the wall approximately 2 metres to your left. One of the kidnappers must have forgot about it.\n")
    time.sleep(0.5)
    slowprint("There's a handgun on the ground about 1,5 metres in front of you.\n")
    time.sleep(0.5)
    slowprint("And some tools hanging from the wall roughly 2 metres to your right-hand side\n")
    time.sleep(0.5)
    slowprint("There's two possible exits, the wall in front you has a door on the right side. And there is a vent in the ceiling close to where the tools are.\n")
  start()
start_game()