import random
import os
from database.cat_facts import catfacts

def create_response(sentence):
    msg = {}
    #Residence Halls
    if sentence == "!hy":
        msg = data['hy']
    if sentence == "!bus":
        msg = data['bus']
    if sentence == "!ttw":
        msg = data['ttw']
    if sentence == "!tte":
        msg = data['tte']
    if sentence == "!fyn":
        msg = data['fyn']
    if sentence == "!fys":
        msg = data['fys']
    if sentence == "!gib":
        msg = data['gib']
    if sentence == "!wil":
        msg = data['wil']
    if sentence == "!hay":
        msg = data['hay']
    if sentence == "!wel":
        msg = data['wel']

    #Cat Facts
    if sentence == '!catfacts':
        num = random.randint(0, (len(catfacts)-1))
        msg = catfacts[num]
                       
    #Responses    
    if "lunch" in sentence.lower():
        msg = "Is it on the PCard?"    
    if "dinner" in sentence.lower():
        msg = "Is it on the PCard?"   
    if "dorm" in sentence.lower():
        msg = "*Residence Hall"

    return msg

data = {
          'hy' : os.getenv('HY'),
          'bus' : os.getenv('BUS'),
          'ttw' : os.getenv('TTW'),
          'tte' : os.getenv('TTE'),
          'fyn' : os.getenv('FYN'),
          'fys' : os.getenv('FYS'),
          'gib' : os.getenv('GIB'),
          'wil' : os.getenv('WIL'),
          'hay' : os.getenv('HAY'),
          'wel' : os.getenv('WEL'),
}
