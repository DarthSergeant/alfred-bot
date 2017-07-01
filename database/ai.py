import os
import random
from database.cat_facts import catfacts

data = {
          hy : os.getenv('HY'),
}


def create_response(sentence):
    msg = {}
    #Residence Halls
    if sentence == "!hy":
        msg = data[hy]
    if sentence == "!bus":
        msg = "Buskirk"
    if sentence == "!ttw":
        msg = TTW
    if sentence == "!tte":
        msg = TTE
    if sentence == "!FYN":
        msg = FYN
    if sentence == "!FYS":
        msg = FYS
    if sentence == "!GIB":
        msg = GIB
    if sentence == "!WIL":
        msg = WIL
    if sentence == "!HAY":
        msg = HAY
    if sentence == "!WEL":
        msg = WEL

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
