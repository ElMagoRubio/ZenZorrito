'''
Created by Manuel González Rubio on the 21-10-2023
Last modified: 22-10-2023

This module specifies the "Clients" class. This class stores a list of clients, as defined in the client.py module. Its only attribute is
    - client_list: A list of clients

To create an object of this class, a CSV file is required.

The methods of this class are the following:
    - __init__: Initializes a list of Client-type objects from a CSV file
    - get_earliest_check_in_date: Retrieves the client whose last check-in date is the earliest from all the clients of the list.
    - get_latest_check_in_date: Retrieves the client whose last check-in date is the latest from all the clients of the list.
    - get_names: Returns a list containing the full names of the clients stored in client_list, alphabetically ordered.
    - get_jobs: Returns a list containing all the unique jobs of the clients stored in client_list, alphabetically ordered.
    - show: Prints all the information from client_list. 
'''

import client
import csv

class Clients:

    #Constructor for CSV files of clients
    def __init__(self, csv_file=None):
        self.client_list = []

        #If there's a valid CSV file
        if csv_file:
            #Opens and the CSV file in read mode ('r')
            with open(csv_file, "r") as file:

                #Loads the CSV contents into the 'data' variable
                data = list(csv.reader(file, delimiter=","))

                #Checks for a client-type CSV file.
                try:
                    if  data[0] == ['First Name', 'Last Name', 'Street', 'Zip', 'City', 'Type', 'Last Check-In Date', 'Job', 'Phone', 'Company']:
                        #Removes the first line, which contains the field names
                        data.pop(0)

                        #Moves the data to a list of clients, using the Client class constructor
                        for current_client in data:
                            print(f'\n{current_client}')
                            aux_client = client.Client(
                                first_name=current_client[0], 
                                last_name=current_client[1], 
                                street=current_client[2], 
                                zip_code=current_client[3], 
                                city=current_client[4], 
                                c_type=current_client[5], 
                                checkin=current_client[6],
                                job=current_client[7], 
                                phone=current_client[8], 
                                company=current_client[9]
                                )
                            self.client_list.append(aux_client)

                    else:
                        raise ValueError('ERROR: CSV file does not contain clients\' data')
                #If the CSV file is not a client file, it prints the error out
                except:
                    print('ERROR: CSV file does not contain clients\' data')
                    self.client_list=[]
                
                #Closes the CSV file
                file.close()
    
    #Returns the client with the earliest check-in date
    def get_earliest_checkin_date(self):
        try:
            #Checks for valid dates (datetime.min is used as non-valid/empty input values)
            min_bool = False
            min = None
            for current_client in self.client_list:
                if min_bool == False:
                    if current_client.checkin != '-':
                        min_bool = True
                        min = current_client
                
                #If there's two valid dates to compare and the current date is later than the current maximum, it updates the return value
                elif current_client.checkin != '-' and current_client.checkin > min.checkin:
                        min = current_client

            #Checks if there was no valid dates in the whole list
            if min == None:
                raise ValueError("ERROR: No valid dates were found")
            
            #Returns the latest valid date found.
            return min
        
        #If there was no valid dates, returns False
        except ValueError:
            print("ERROR: No valid dates were found")
            return False
    
    #Returns the Client object whose last checkin attribute is the latest.
    def get_latest_checkin_date(self):
        try:
            #Checks for valid dates (datetime.min is used as non-valid/empty input values)
            max_bool = False
            max = None
            for current_client in self.client_list:
                if max_bool == False:
                    if current_client.checkin != '-':
                        max_bool = True
                        max = current_client
                
                #If there's two valid dates to compare and the current date is later than the current maximum, it updates the return value
                elif current_client.checkin != '-' and current_client.checkin > max.checkin:
                        max = current_client

            #Checks if there was no valid dates in the whole list
            if max == None:
                raise ValueError("ERROR: No valid dates were found")
            
            #Returns the latest valid date found.
            return max
        
        #If there was no valid dates, returns False
        except ValueError:
            print("ERROR: No valid dates were found")
            return False
    
    #Returns a list containing the full names of the clients stored in client_list, alphabetically ordered. It ignores empty values
    def get_names(self):
        try:
            #Initializes the list of names, excluding empty ('-') values
            names = [[client.last_name, client.first_name] for client in self.client_list if client.first_name != '-' and client.last_name != '-']

            #Checks the list is not empty
            if not names:
                raise ValueError("ERROR: No clients found")

            #Sorts the list of names
            sorted_names = sorted(names,key=lambda x: (x[0], x[1]))
        
            #Returns the ordered list
            return sorted_names
        
        #If the list is empty, returns False
        except ValueError:
            print("ERROR: No clients found")
            return False

    #Returns a list containing all the unique jobs of the clients stored in client_list, alphabetically ordered. It ignores empty values.
    def get_jobs(self):
        try:
            #Initializes the set of jobs, excluding empty ('-') values
            jobs={client.job for client in self.client_list if client.job != '-'}

            #Checks the list is not empty
            if not jobs:
                raise ValueError("ERROR: No clients found")

            #Sorts the set of jobs
            sorted_jobs = sorted(jobs,key=lambda x: (x[0]))

            #Returns the ordered set
            return sorted_jobs
        
        #If there were no valid jobs, returns False
        except ValueError:
            print("ERROR: No clients found")
            return False
    
    #This function is used to properly print all the clients in the list, using client.show()
    def show(self):
        if self.client_list:
            for client in self.client_list:
                client.show()
        else:
            print("No clients found")
