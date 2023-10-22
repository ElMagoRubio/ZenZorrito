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
                if data[0][0] == 'First Name':
                    #Removes the first line, which contains the field names
                    data.pop(0)

                    #Moves the data to a list of clients, using the Client class constructor
                    for current_client in range(len(data)):
                        print(f'\n{data[current_client]}\n')
                        aux_client = client.Client(
                            first_name=data[current_client][0], 
                            last_name=data[current_client][1], 
                            street=data[current_client][2], 
                            zip_code=data[current_client][3], 
                            city=data[current_client][4], 
                            c_type=data[current_client][5], 
                            checkin=data[current_client][6],
                            job=data[current_client][7], 
                            phone=data[current_client][8], 
                            company=data[current_client][9]
                            )
                        self.client_list.append(aux_client)

                #If the CSV file is not a client file, it prints the error out
                else:
                    print('ERROR: CSV file does not contain clients\' data')
                
                #Closes the CSV file
                file.close()
    
    #Returns the client with the earliest check-in date
    def get_earliest_checkin_date(self):
        #Checks for valid dates (datetime.min is used as non-valid/empty input values)
        min_bool = False
        min = None
        for current_client in range(len(self.client_list)):
            if min_bool == False:
                if self.client_list[current_client].checkin != '-':
                    min_bool = True
                    min = self.client_list[current_client]
            
            #If there's two valid dates to compare and the current date is prior to the current minimum, it updates the return value
            elif self.client_list[current_client].checkin != '-' and self.client_list[current_client].checkin < min.checkin:
                    min = self.client_list[current_client]

        #Returns the earliest date found. If no valid date was found, it returns a None value.
        return min
    
    #Returns the Client object whose last checkin attribute is the latest.
    def get_latest_checkin_date(self):
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

        #Returns the latest date found. If no valid date was found, it returns a None value.
        return max
    
    #Returns a list containing the full names of the clients stored in client_list, alphabetically ordered. It ignores empty values
    def get_names(self):
        #Initializes the list of names, excluding empty ('-') values
        names = [[client.last_name, client.first_name] for client in self.client_list if client.first_name != '-' and client.last_name != '-']

        #Sorts the list of names
        sorted_names = sorted(names,key=lambda x: (x[0], x[1]))

        #Returns the ordered list
        return sorted_names

    #Returns a list containing all the unique jobs of the clients stored in client_list, alphabetically ordered. It ignores empty values.
    def get_jobs(self):
        #Initializes the set of jobs, excluding empty ('-') values
        jobs={client.job for client in self.client_list if client.job != '-'}

        #Sorts the set of jobs
        sorted_jobs = sorted(jobs,key=lambda x: (x[0]))

        #Returns the ordered set
        return sorted_jobs
    
    #This function is used to properly print all the clients in the list, using client.show()
    def show(self):
        for client in self.client_list:
            client.show()
