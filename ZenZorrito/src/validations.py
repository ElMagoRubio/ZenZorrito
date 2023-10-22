'''
Created by Manuel González Rubio on the 20-10-2023
Last modified: 21-10-2023

This module is meant to be used as an auxiliary module for validating "Client" class attributes. It contains the following functions:
    - nonempty_field_vld: Validates that a field is not empty
    - zipcode_vld: Validates the client's zip code. It only validates the Spanish zip code standard. If need be, it could be expanded accept to other countries standards.
    - type_vld: Validates the client's type. The type must be one of the following letters: A,D,U
    - phone_vld: Validates a phone number. It only validates the Spanish telephone standard. If need be, it could be expanded to accept other countries standards
    - date_vld: Validates a date. It needs to follow the dd-mm-yyyy or dd/mm/yyyy format. It uses the datetime module. As no hour is introduced in the CSV, it will always show it as 00:00:00

Every incorrect field will return '-' as its value. If the field is correctly validated, it will return the original value.
'''


import re
from datetime import datetime

#Validates non-empty fields. If empty, it prints out which field is empty
def nonempty_field_vld(field, value):
    if value == '':
        print(f"WARNING: Client's {field} field is empty. Will input '-' as value")
        value = '-'
    return value


#Validates zip codes
def zipcode_vld(zip_code):
    #If the zip code is not unknown or is not a 5 number code, it prints an error
    if not re.match(r'^\d{5}$', zip_code) and zip_code != '-': 
        print("WARNING: Invalid zip code, must be 5 digit code. Will input '-' as value")
        zip_code = '-'

    return zip_code

#Validates client type
def type_vld(c_type):
    c_type.capitalize()
    #If the client type is not unknown or is not a letter, it prints an error
    if not re.match(r'^[ADU]$', c_type) and c_type != '-':
        print("WARNING: Invalid client type. Must be one of the following letters: A, D, U. Will input '-' as value")
        c_type = '-'

    return c_type

#Validates telephones in the spanish format
def phone_vld(phone):
    #Sanitizes the number so as not to have spaces nor spanish country prefix in the final value
    phone = phone.replace(" ", "")
    phone = phone.replace("+34", "")

    #If the telephone is not unknown or is not a 9 number code, it prints an error
    if not re.match(r'^\d{9}$', phone) and phone != '-':
        print("WARNING: Invalid phone, must comply with the Spanish phone format:(+34) XXX XXX XXX. Will input '-' as value")
        phone = '-'

    return phone

#Validates dates such that it follows dd/mm/yyyy format or dd-mm-yyyy format
def date_vld(checkin):
    #Changes - to /. This is made for consistency
    checkin = checkin.replace("-", "/")

    #If the date is not unknown or valid, it prints an error
    if not re.match(r'^(0?[1-9]|[12][0-9])\/(0?[1-9]|1[0-2])\/\d{4}$', checkin) and not re.match(r'^30\/(0?[13-9]|1[0-2])\/\d{4}$', checkin) and not re.match(r'^(31)\/(0?[13578]|1[02])\/\d{4}$', checkin) and checkin != '/': 
        print("WARNING: Invalid check-in date, must comply with the following formats: dd/mm/yyyy, dd-mm-yyyy. Will input '-' as value")
        checkin_date = '-'
    else:
        try:
            checkin_date = datetime.strptime(checkin, "%d/%m/%Y")
        
        except ValueError:
            ("WARNING: Check-in date must be a valid date. Will input '-' as value")
            checkin_date = datetime.min
    
    return checkin_date