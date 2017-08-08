"""##########################
# Imports
##########################"""
from hrl.information.office_hours import *
from hrl.information.august import *
from hrl.information.september import*
from hrl.information.october import *
from hrl.information.november import*
from hrl.information.december import *

"""##########################
# Classes
##########################"""
class Rd:
    def __init__(self, office_number, cell_number, email, monday, tuesday, wednesday, thursday, friday):

        self.office_number = office_number
        self.cell_number = cell_number
        self.email = email

        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday

Rd_sam = Rd('sam_office', 'sam_cell', 'sam_email', sam_monday[0], sam_tuesday[0], sam_wednesday[0], sam_thursday[0], sam_friday[0])
Rd_gabe = Rd('gabe_office', 'gabe_cell', 'gabe_email', gabe_monday[0], gabe_tuesday[0], gabe_wednesday[0], gabe_thursday[0], gabe_friday[0])
Rd_meena = Rd('meena_office', 'meena_cell', 'meena_email', meena_monday[0], meena_tuesday[0], meena_wednesday[0], meena_thursday[0], meena_friday[0])

class Duty:
    def __init__(self, commons_duty, holderby_duty):
        
        self.commons_duty = commons_duty
        self.holderby_duty = holderby_duty
        
#Note - commons_august and all the other definitions below are imported from duty folder
Duty_august = Duty(commons_august, holderby_august)
Duty_september = Duty(commons_september, holderby_september)
Duty_october = Duty(commons_october, holderby_october)
Duty_november = Duty(commons_november, holderby_november)
Duty_december = Duty(commons_december, holderby_december)

#Duty_august.commons_duty[n] will bring up day n on the calendar
#Edity the duty definitions to reflect this slight change in wording 

"""##########################
# Heroku Definitions
##########################"""   
ac_duty_phone = 'ac_duty_phone'
mupd = 'mupd'
hayman_duty = 'hayman_duty'
gillis_duty = 'gillis_duty'
holderby_duty = 'holderby_duty'
holderby_desk = 'holderby_desk'
wellman_desk = 'wellman_desk'
haymaker_desk = 'haymaker_desk'
willis_desk = 'willis_desk'
gibson_desk = 'gibson_desk'
what_building = 'please specify building'

"""##########################
# Word Database 
##########################"""    
#The naming convention is this:
#The first term is what the list contains
#The second term is the type of list
	#Search is a list of strings that functions use to search the text
	#Data is either a list of variables for conversion purposes or a uniform term for the things in the search

hrl_words = [''] #######@@@@@@@@@@@@ put this at top at end.   List of words from other lists.  Used to determine when HRL functions should be used in bot.

question_search = ['who', 'what', 'when', 'where', 'why', '?']

name_search = ['gabe', 'sam', 'meena']
name_data = [Rd_gabe, Rd_sam, Rd_meena]

number_search = ["number", "num", '#', 'phone', 'cell']


week_search = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
day_search = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '10',
              '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
day_data = [11, 12, 13, 14, 15, 16, 17, 18, 19, 10, 
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
email_search = ['email', 'e-mail'] 
email_data = ['email', 'email']

biweekly_search = ['bi-weekly', 'biweekly', 'bi', 'weekly']
biweekly_data = ['biweekly', 'biweekly', 'biweekly', 'biweekly']

month_search = [#'jan', 'feb', 'mar', 'apr', 'may', 'june', 'july',
                'aug', 'sept', 'oct', 'nov', 'dec'] #prior line is for spring semesters so noted out
month_data = [#Duty_january, Duty_february, Duty_march, Duty_april, Duty_may, Duty_june, Duty_july,
              Duty_august, Duty_september, Duty_november, Duty_december] #prior line is for spring semesters

phone_search = ['office', 'cell']
phone_data = ['office_number', 'cell_number']

title_search = ['ac', 'aac', 'rd', 'ard']
title_data = [ac_duty_phone, ac_duty_phone, ac_duty_phone, ac_duty_phone]

building_search = ['michelle', 'michaelle', 'nicole', 'ruth', 'ann', 'hy', 'hol',
					'gn', 'gib', 'wn', 'wel', 'hay', 'wil', 'ws']
desk_data =  [holderby_desk, holderby_desk, what_building, what_building, what_building, holderby_desk, holderby_desk, 
			  gibson_desk, gibson_desk, wellman_desk, wellman_desk, haymaker_desk, willis_desk, willis_desk]
duty_data = [None, None, None, None, None, holderby_duty, holderby_duty, 
	    gillis_duty, gillis_duty, hayman_duty, hayman_duty, hayman_duty, gillis_duty, gillis_duty]
							  
"""##########################
# Specify Functions
##########################"""             
    #These function narrows down a message into specific key words or converts string into a usable variable
	
def specify_list(text, search, data):
    for i in range(len(search)): #searches the strings
        if search[i] in text:
            return(data[i]) #returns the relevant term based off of the search 
			      
"""##########################
# Determinations
##########################"""
	#These functions determine what information to send back
def determine_duty_info(text): #perhaps use a determine function like in the above to find the month and day to feed into this one
    if 'duty' in text: #other function only filters by who, this ensures the who was actually about duty
        for i in range(len(month_search)):
            if month_search[i] in text:
                for n in range(len(day_search)):
                    if day_search[n] in text:
                        day = day_data[n]-1 #-1 b/c the 1st on actual calendar is really position 0
                        month = specify_list(text, month_search, month_data)
                        if "com" in text: #or com or whatever
                            return(month.commons_duty[day])
                        if "hol" in text: #or whatever other abbreviations maybe use a search function for both of these
                            return(month.holderby_duty[day])
                        else:

                            return(month.commons_duty[day] +
                                   month.holderby_duty[day])                  
            else:
                return("Please specify month and day.")	 
				
def determine_numbers(text):
	#if any(word in text for word in number_search): #Should be taken care of in the delegate function
		#MUPD
                if 'mupd' in text:
                    return(mupd)
		#RD Office or Cell
                elif any(word in text for word in name_search): #check if they want RD info
                    if any(word in text for word in phone_search):
                        if specify(text, phone_search, phone_data) ==  'office_number': #return RD office number
                            return(specify_list(text, name_search, name_data).office_number)
                        elif specify(text, phone_search, phone_data) == 'cell_number': #return RD cell number
                            return(specify_list(text, name_search, name_data).cell_number)
                        else:
                            return(specify_list(text, name_search, name_data).cell_number) #if nothing specified but RD number was searched for, defaults to cell
		#Duty Phone
                elif 'duty' in text: 
                    if any(word in text for word in title_search): #searches for AC duty phone 
                        return(specify_list(text, title_search, title_data))
                    elif any(word in text for word in building_search):
                        return(specify_list(text, building_search, duty_data))
		#Front Desk Numbers
                elif any(word in text for word in building_search): 
                    return(specify_list(text, building_search, desk_data)) #should return the front desk number
					   			
def determine_email(text):
	return(specify_list(text, name_search, name_data).email)
	
def determine_office_hours(text):
    if any(word in text for word in week_search): #searches if day specified
        if 'mon' in text:
            return(specify_list(text, name_search, name_data).monday)
        elif 'tue' in text:
            return(specify_list(text, name_search, name_data).tuesday)
        elif 'wed' in text:
            return(specify_list(text, name_search, name_data).wednesday)
        elif 'thur' in text:
            return(specify_list(text, name_search, name_data).thursday)
        elif 'fri' in text:
            return(specify_list(text, name_search, name_data).friday)
        else:
            return("Week Error - Value Not Found")
    else: #if day not specified gives all info
        return(specify_list(text, name_search, name_data).monday+
               specify_list(text, name_search, name_data).tuesday+
               specify_list(text, name_search, name_data).wednesday+
               specify_list(text, name_search, name_data).thursday+
               specify_list(text, name_search, name_data).friday)

"""##########################
# HRL Responses
##########################"""
    #This function sorts message into the proper category
    #It also serves to condense everything in this file to a single easily exported function
def delegate_message(text):
	#Is it a question?
        if any(word in text for word in question_search): #Check if question
                    #Duty Calendar
            if 'who' in text: #check for word am as well for "am I on duty on x
                return(determine_duty_info(text))
                    #Numbers
            elif any(word in text for word in number_search):
                return(determine_numbers(text))
                        #SPLIT - Function below here go through a name search because they require a name to run
            elif any(word in text for word in name_search): 
                    #Email
                if any(word in text for word in email_search): 
                    return(determine_email(text))
                    #Office Hours
                if 'office' in text:
                    if any(word in text for word in name_search):
                        return(determine_office_hours(text))
                    #Bi-Weekly
                '''$$$ UNDER CONSTRUCTION $$$'''
			






