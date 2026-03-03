from Redacted_list import my_username
import random
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  print(user_message)
  if "BOT_NOAH" in user_message:
    return True
  elif "I didn't say you were":
     return True
  elif "calm down":
     return True
  elif "OKAY YOU'RE CLEARLY ON IT!!!":
    return True
  elif "AHHH":
     return True
  elif "Can you say anything else?!?":
     return True
  elif "THE ISLAND?!?":
     return True
  elif "umm ok?":
     return True
  elif "Bro really":
     return True
  elif "Care to explain the photo":
     return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""

def respond(user_message, user_name):
    c =["NOAH's NOT ON THE LIST", "Noah did no wrong", "Why would assume he's on it?!?", "Noah isn't like that"]
    w = random.choice(c)
    return w
    {user_message.replace("BOT_NOAH", user_name)}