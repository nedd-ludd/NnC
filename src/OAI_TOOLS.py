#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-02-13
"""
import os

#WARNING: THIS FILE CONTAINS THE INSTRUCTION STORED IN OpenAI's ASSISTANT VIA DEVELOPER PORTAL, IT HERE FOR REFERENCE ONLY

##OpenAI Client
NAME = "NnC (Nancy) Nextcloud Calendar Assistant"
START_INSTRUCT = """
    You are an AI assistant that manages a user's Nextcloud calendar via WebDAV. 
    Your role is to help users create, retrieve, update, and delete calendar events 
    in compliance with the iCalendar (RFC 5545) standard.

    You must:
    - Structure all events using proper ISO 8601 date-time formats.
    - Call the correct function dynamically based on user intent.
    - Ensure event metadata (timestamps, categories, transparency, etc.) follows iCalendar standards.
    - Maintain accurate time zone handling and recurrence support.
    - Provide clear responses about event details when queried.
    
    If a user requests to schedule, modify, or delete an event, use function calling 
    to process the request. If an event lookup is needed, fetch and return relevant details.
    
    DO NOT fabricate event details. Only return data that exists in the Nextcloud calendar.
    If an event cannot be found, inform the user accordingly.
    """

#Function Calls
CREATE = {
    "name": "create_calendar_event",
    "description": "Create an iCalendar event using RFC 5545 fields. This function returns a non-allday event, i.e has DTSTART and DTEND in ISO 8601 format.",
    "parameters": {
        "type": "object",
        "properties": {
            "VERSION": {
                "type": "string",
                "description": "iCalendar format version. Default '2.0'."
            },
            "CALSCALE": {
                "type": "string",
                "description": "Defines the calendar scale. Default is 'GREGORIAN'."
            },
            "PRODID": {
                "type": "string",
                "description": "Identifier of the software that created the calendar entry. Default is '-//Nancy AI//NONSGML NnC Assistant v1.0//EN'"
            },
            "SUMMARY": {
                "type": "string",
                "description": "Short summary or title of the event."
            },
            "DTSTAMP": {
                "type": "string",
                "format": "date-time",
                "description": "Timestamp when the event was created or last updated (ISO 8601 format)."
            },
            "DTSTART": {
                "type": "string",
                "format": "date-time",
                "description": "Start date and time of the event (ISO 8601 format)."
            },
            "DTEND": {
                "type": "string",
                "format": "date-time",
                "description": "End date and time of the event (ISO 8601 format)."
            },
            "LOCATION": {
                "type": "string",
                "description": "The location where the event takes place."
            },
            "DESCRIPTION": {
                "type": "string",
                "description": "Detailed description of the event."
            },
            "STATUS": {
                "type": "string",
                "enum": ["TENTATIVE", "CONFIRMED", "CANCELLED"],
                "description": "The status of the event."
            },
            "CLASS": {
                "type": "string",
                "enum": ["PUBLIC", "PRIVATE", "CONFIDENTIAL"],
                "description": "Visibility classification of the event. Usually PRIVATE"
            },
            "TRANSP": {
                "type": "string",
                "enum": ["OPAQUE", "TRANSPARENT"],
                "description": "Defines whether the event blocks time on the calendar. Usually OPAQUE "
            },
            "CATEGORIES": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Categories or tags associated with the event."
            },
            "SEQUENCE": {
                "type": "integer",
                "description": "Revision sequence number for the event updates."
            }
        },
        "required": ["VERSION", "PRODID", "UID", "DTSTAMP", "DTSTART", "DTEND", "SUMMARY"]
    }
}

# "UID": { #gen_uid.py
#     "type": "string",
#     "description": "Globally unique identifier for the event."
# },

# CREATE_ALLDAY = {}
# CANCEL = {}
# DELETE = {}
# MODIFY = {}
# FIND = {}
# FIND_MANY = {}

#PREFERENCES
#WARNING: HAVE THESE AS SEPERATE JSON AND TEXT FILES.
FINE_TUNE = {} 
# List of habits
#Usually my morning routine events are transparent, so any major potential bookings would not conflict.
#If booking in a trip, i would usually need travel time
# Medical appointments are set to OPAQUE and PRIVATE 
# NOTE:should medical appointments be set to confidential.
#CLUSTER bookings


FUNC_CALLS = [CREATE] #TODO: ADD RESE

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)

if __name__ == '__main__':
    main()