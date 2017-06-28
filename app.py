#Note, this bot was created to respond to a friend in chat who repeats same pictures and phrases

import os
import sys
import json
import random          
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

from database.cat_facts import catfacts

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  sentence = data['text']

#############################################
  if "dorm" in sentence.lower():
           msg = "*Residence Hall"
           send_message(msg)
  if "lunch" in sentence.lower():
           msg = "Is it on the PCard?"
           send_message(msg)
  if "dinner" in sentence.lower():
          msg = "Is it on the PCard?"
          send_message(msg)
  if sentence == '!catfacts':
    num = random.randint(0, (len(catfacts)-1))
    msg = catfacts[num]
    send_message(msg)
    



#########################################
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
sys.stdout.flush()
