import os
import sys
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

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
      
return "ok", 200
def post_response_inner(text):
  if "cat" in text:
    return("cat")
