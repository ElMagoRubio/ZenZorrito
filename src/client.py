from datetime import date
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
            'job': '',
            'phone': '',
            'check_in': '',
            'company': ''
        }
        for key in defaults:
            setattr(self, key, 'Unknown')

        for key, value in keys.items():
            setattr(self, key, value)

    
    #Getter for client's first name
    @property
    def first_name(self):
        return self._first_name

    #Setter for client's first name. It capitalizes the first letter of each name
    @first_name.setter
    def first_name(self, value):
        value = value.title()
        self._first_name = value


    #Getter for client's last name
    @property
    def last_name(self):
        return self._last_name

    #Setter for client's first name. It capitalizes the first letter of each name
    @last_name.setter
    def last_name(self, value):
        value = value.title()
        self._last_name = value


    #Getter for client's street. 
    @property
    def street(self):
        return self._street
    
    #Setter for client's street. It capitalizes the first word.
    @street.setter
    def street(self, value):
        value = value.capitalize()
        self._street = value
    

    #Getter for client's zip code. 
    @property
    def zip_code(self):
        return self._zip_code

    #Setter for client's zip code. It validates it with validations.zipcode_vld() function
    @zip_code.setter
    def zip_code(self, value):
        value = validations.zipcode_vld(value)
        self._zip_code = value


    #Setter for client's city.
    @property
    def city(self):
        return self._city

    #Setter for client's zip code. It capitalizes each word of the city
    @city.setter
    def city(self, value):
        value = value.title()
        self._city = value


    #Getter for client's type
    @property
    def c_type(self):
        return self._c_type

    #Setter for client's type. It validates it with validations.type_vld() function
    @c_type.setter
    def c_type(self, value):
        value = validations.type_vld(value)
        self._c_type = value


    #Getter for client's job
    @property
    def job(self):
        return self._job

    #Setter for client's job. It capitalizes it
    @job.setter
    def job(self, value):
        value = value.capitalize()
        self._job = value


    #Getter for the client's phone
    @property
    def phone(self):
        return self._phone

    #Setter for client's phone. It validates it with validations.phone_vld() function
    @phone.setter
    def phone(self, value):
        value = validations.phone_vld(value)
        self._phone = value


    #Getter for client's phone.
    @property
    def check_in(self):
        return self._check_in

    #Setter for client's phone. It validates it with validations.date_vld() function
    @check_in.setter
    def check_in(self, value):
        value = validations.date_vld(value)
        self._check_in = value
    


    #Getter for client's phone.
    @property
    def company(self):
        return self._company

    #Setter for client's city. It capitalizes each of the words
    @city.setter
    def company(self, value):
        value = value.title()
        self._company = value


    #This function prints all the attributes of the client.
    def show(self):
        print(f"First name: {self.first_name}\tLast name: {self.last_name}\tStreet: {self.street}\tZip Code: {self.zip_code}\tCity: {self.city}\tType: {self.c_type}\tJob: {self.job}\tPhone: {self.phone}\tLast check in date: {self.check_in}\tCompany: {self.company}")
