import random
from database.cat_facts import catfacts

def create_response(sentence):
    msg = {}
    #Residence Halls
    if sentence == "!HY":
        msg = HY
    if sentence == "!BUS":
        msg = BUS
    if sentence == "!TTW":
        msg = TTW
    if sentence == "!TTE":
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
        send_message(msg)

    #Responses    
    if "lunch" in sentence.lower():
        msg = "Is it on the PCard?"
        send_message(msg)
    if "dinner" in sentence.lower():
        msg = "Is it on the PCard?"
        send_message(msg)
    if "dorm" in sentence.lower():
        msg = "*Residence Hall"
        send_message(msg)

    return msg
