'''
Created by Manuel González Rubio on the 20-10-2023
Last modified: 21-10-2023

This module specifies the "Client" class. This class is used for storing individual clients. Each client will have the following attributes:
    - first_name: Client's first name. 
    - last_name: Client's last name.
    - street: Client's street of residence
    - zip_code: Client's zip code. Must be a 5 letter digit code, in order to comply with Spanish zip code regulation.
    - city: Client's city of residence
    - c_type: Client's type. Must be one of the following letters: A, D, U.
    - checkin: Client's last check-in date. Must comply with the dd-mm-yyyy or dd/mm/yyyy format. Stored as dd/mm/yyyy
    - job: Client's job
    - phone: Client's phone number. Must follow the Spanish standard: +34 XXX XXX XXX, in which each X is a number. The country prefix is optional. Stored as XXXXXXXXX
    - company: Client's company.

For field validation, we make use of "validations.py", a custom module created exclusively for this class. If a field is either empty or non-valid, it is stored as '-' in its corresponding attribute.
'''

import validations


class Client:
    
    #Class constructor with parameters for each attribute, with defaults for each one
    def __init__(self, **keys):
        defaults = {
            'first_name': '',
            'last_name': '',
            'street': '',
            'zip_code': '',
            'city': '',
            'c_type': '',
            'checkin': '',
            'job': '',
            'phone': '',
            'company': ''
        }
        for key in defaults:
            setattr(self, key, '-')

        for key, value in keys.items():
            setattr(self, key, value)

    
    #Getter for client's first name
    @property
    def first_name(self):
        return self._first_name

    #Setter for client's first name. It capitalizes the first letter of each name
    @first_name.setter
    def first_name(self, value):
        value = validations.nonempty_field_vld('first name', value)
        value = value.title()
        self._first_name = value


    #Getter for client's last name
    @property
    def last_name(self):
        return self._last_name

    #Setter for client's first name. It capitalizes the first letter of each name
    @last_name.setter
    def last_name(self, value):
        value = validations.nonempty_field_vld('last name', value)
        value = value.title()
        self._last_name = value


    #Getter for client's street. 
    @property
    def street(self):
        return self._street
    
    #Setter for client's street. It capitalizes the first word.
    @street.setter
    def street(self, value):
        value = validations.nonempty_field_vld('street', value)
        value = value.capitalize()
        self._street = value
    

    #Getter for client's zip code. 
    @property
    def zip_code(self):
        return self._zip_code

    #Setter for client's zip code. It validates it with validations.zipcode_vld() function
    @zip_code.setter
    def zip_code(self, value):
        value = validations.nonempty_field_vld('zip code', value)
        value = validations.zipcode_vld(value)
        self._zip_code = value


    #Setter for client's city.
    @property
    def city(self):
        return self._city

    #Setter for client's zip code. It capitalizes each word of the city
    @city.setter
    def city(self, value):
        value = validations.nonempty_field_vld('city', value)
        value = value.title()
        self._city = value


    #Getter for client's type
    @property
    def c_type(self):
        return self._c_type

    #Setter for client's type. It validates it with validations.type_vld() function
    @c_type.setter
    def c_type(self, value):
        value = validations.nonempty_field_vld('type', value)
        value = validations.type_vld(value)
        self._c_type = value


    #Getter for client's job
    @property
    def job(self):
        return self._job

    #Setter for client's job. It capitalizes it
    @job.setter
    def job(self, value):
        value = validations.nonempty_field_vld('job', value)
        value = value.capitalize()
        self._job = value


    #Getter for the client's phone
    @property
    def phone(self):
        return self._phone

    #Setter for client's phone. It validates it with validations.phone_vld() function
    @phone.setter
    def phone(self, value):
        value = validations.nonempty_field_vld('phone number', value)
        value = validations.phone_vld(value)
        self._phone = value


    #Getter for client's phone.
    @property
    def checkin(self):
        return self._checkin

    #Setter for client's phone. It validates it with validations.date_vld() function
    @checkin.setter
    def checkin(self, value):
        value = validations.nonempty_field_vld('last check-in date', value)
        value = validations.date_vld(value)
        self._checkin = value
    


    #Getter for client's company.
    @property
    def company(self):
        return self._company

    #Setter for client's company. It capitalizes each of the words
    @company.setter
    def company(self, value):
        value = validations.nonempty_field_vld('company', value)
        value = value.title()
        self._company = value


    #This function prints all the attributes of the client.
    def show(self):
        print(f"First name: {self.first_name}\nLast name: {self.last_name}\nStreet: {self.street}\nZip Code: {self.zip_code}\nCity: {self.city}\nType: {self.c_type}\nJob: {self.job}\nPhone: {self.phone}\nLast check in date: {self.checkin}\nCompany: {self.company}\n\n")
