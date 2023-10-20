import re

#Validates zip codes
def zipcode_vld(zip_code):
    #If the zip code is not unknown or is not a 5 number code, it prints an error
    if not re.match(r'^\d{5}$', zip_code) and zip_code != 'Unknown': 
        print("ERROR: Invalid zip code, must be 5 digit code")
        zip_code = 'Unknown'

    return zip_code

#Validates client type
def type_vld(c_type):
    #If the client type is not unknown or is not a letter, it prints an error
    if not re.match(r'^[A-Za-z]$', c_type) and c_type != 'Unknown':
        print("ERROR: Invalid client type. Must only contain 1 letter")
        c_type = 'Unknown'

    return c_type

#Validates telephones in the spanish format
def phone_vld(phone):
    #Sanitizes the number so as not to have spaces nor spanish country prefix
    phone = phone.replace(" ", "")
    phone = phone.replace("+34", "")

    #If the telephone is not unknown or is not a 9 number code, it prints an error
    if not re.match(r'^\d{9}$', phone) and phone != 'Unknown':
        print("ERROR: Invalid phone, must comply with the Spanish phone format: (+34) XXX XXX XXX")
        phone = 'Unknown'

    return phone

#Validates dates such that it follows dd/mm/yyyy format or dd-mm-yyyy format
def date_vld(date):
    #Changes - to /. This is made for consistency
    date = date.replace("-", "/")

    #If the date is not unknown or valid, it prints an error
    if not re.match(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$', date) and date != 'Unknown': 
        print("ERROR: Invalid check_in date, must comply with the following formats:\ndd/mm/yyyy\ndd-mm-yyyy")
        date = 'Unknown'
    
    return date