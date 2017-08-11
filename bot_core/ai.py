"""##########################
# Imports
##########################"""
from hrl.hrl_processing import export_hrl_response

"""##########################
# Bot Core
##########################"""
#create a function to determine which database to read from
def post_response(text):
        if "cat" in text:
                return("cat")
                   
        #return(export_hrl_response(text))

#def find_database(text):
#	if any(word in text for word in )
