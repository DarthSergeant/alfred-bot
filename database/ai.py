import random
import os
from database.cat_facts import catfacts
from database.office_hours import *

"""##########################
# Temporary 8 Ball
##########################"""
eight_ball = ['It is certain', ' It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it'
              'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
              'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
              'Concentrate and ask again', 'Dont conunt on it', 'My reply is no', 'My sources say no',
              'Outlook not so good', 'Very doubtful']

    
class Rd:
    def __init__(self, office_number, phone_number, email, monday, tuesday, wednesday, thursday, friday):

        self.office_number = office_number
        self.phone_number = phone_number
        self.email = email

        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday

Rd_sam = Rd('HKofficenum', 'HKphone', 'HKemail', sam_monday[0], sam_tuesday[0], sam_wednesday[0], sam_thursday[0], sam_friday[0])
Rd_gabe = Rd('HKofficenum', 'HKphone', 'HKemail', gabe_monday[0], gabe_tuesday[0], gabe_wednesday[0], gabe_thursday[0], gabe_friday[0])
Rd_meena = Rd('HKofficenum', 'HKphone', 'HKemail', meena_monday[0], meena_tuesday[0], meena_wednesday[0], meena_thursday[0], meena_friday[0])

"""##########################
# Information Section
##########################"""
#   This is where information will be stored.

"""##########################
# Word Database 
##########################"""
    #Contains words that are referenced or searched in the functions

question_words = ['who', 'what', 'when', 'where', 'why', '?']

type_search = ['number', 'phone', 'email', 'e-mail', 'hours', 'office number']
type_data = ['phone_number', 'phone_number', 'email', 'email', 'office_hours', 'office_number']

name_search = ['gabe', 'sam', 'meena']
name_data = [Rd_gabe, Rd_sam, Rd_meena]

week_search = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
week_data = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

"""##########################
# Determinations
##########################"""
    #Searches text for specific words and tweaks them into a usable reference 

    #This one searches for word in the string then converts it usable data
def determine_type(text):
    for i in range(len(type_search)):
        if type_search[i] in text:
            return(type_data[i])
        
    #This one converts synonyms into a single word for reference
    #For example, number and phone would both be converted to phone_number
def determine_name(text):
    for i in range(len(name_search)):
        if name_search[i] in text:
            return(name_data[i])

def determine_week(text):
    for i in range(len(week_search)):
        if week_search[i] in text:
            return(week_data[i])
       
"""##########################
# Determinations
##########################"""

def post_response(text):
    #The next function could do this one's role, but seperating it may help in the future
    return(determine_if_active(text))
       
def determine_if_active(text):
    if '!8ball' in text:
        num = random.randint(0, (len(eight_ball)-1))
        return(eight_ball[num])
    #if any(word in text for word in question_words): #Check if question
     #   if any(word in text for word in name_search): #Check if they're asking about person
      #      if any(word in text for word in type_search): #Check that  they're looking for something in there is info on
       #         return(response_type(text))
    
def response_type(text):
    #You can't enter type as second half of statement on next line, so each must be written individualy
    if determine_type(text) == 'phone_number': 
        return(determine_name(text).phone_number)
    elif determine_type(text) == 'office_number':
        return(determine_name(text).office_number)
    elif determine_type(text) == 'email':
        return(determine_name(text).email)   
    elif determine_type(text) == 'office_hours':
        return(determine_office_hours(text))
          
    #Office Hours is a bit more complicated than the others, so it is seperated into a different function for readability
def determine_office_hours(text):
    if any(word in text for word in week_search): #searches if day specified
        if determine_week(text) == 'monday':
            return(determine_name(text).monday)
        elif determine_week(text) == 'tuesday':
            return(determine_name(text).tuesday)
        elif determine_week(text) == 'wednesday':
            return(determine_name(text).wednesday)
        elif determine_week(text) == 'thursday':
            return(determine_name(text).thursday)
        elif determine_week(text) == 'friday':
            return(determine_name(text).friday)
        else:
            return("Unknown Error - Value Not Found")
    else: #if day not specified gives all info
        return(determine_name(text).monday+
               determine_name(text).tuesday+
               determine_name(text).wednesday+
               determine_name(text).thursday+
               determine_name(text).friday)
