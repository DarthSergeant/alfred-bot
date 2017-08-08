'''This imports a single function from information_processing to avoid extra
import clutter from the other files saved in the information files.

This file is then the one that is read by the main bot, keeping the main bot from
touching anything in the hrl file except for this exported response.
'''

"""##########################
# Imports
##########################"""
import os

from hrl.information_processing import delegate_message

"""##########################
# HRL Responses
##########################"""
def export_hrl_response(text): 
	return(delegate_message(text))


