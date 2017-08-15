import os
import sys
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

#from bot_core.ai import post_response
from outer.cat2 import post_response
global TEXT

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  raw_name = data['name']
  raw_text = data['text']
  #This saves the lowercase version as something else
  name = raw_name.lower()
  text = raw_text.lower()
  TEXT = text 
  response = post_response(text)
  if response:
    if name != "alfred bot":
      send_message(response)
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
