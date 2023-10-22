'''
Created by Manuel González Rubio on the 21-10-2023
Last modified: 22-10-2023

This module is used to show how to use the methods for "Clients". 
To execute from terminal: $python3 main.py "csv-file path relative to main.py"
There is also a makefile that automates some tasks, such as the execution of this file
'''

import clients as c
import os
import argparse


def main():
    #Create an argument parser
    parser = argparse.ArgumentParser(description='Procesar archivo CSV de clientes')
    
    #Add an argument for CSV file's path
    parser.add_argument('csv_file', help='Ruta al archivo CSV de clientes')
    
    #Parse arguments from command line
    args = parser.parse_args()

    #Create the path for the csv file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "../", args.csv_file)

    #Create a list of clients from csv file
    clients = c.Clients(csv_file)

    #Shows clients' list
    clients.show()

    #Earliest check-in date
    print(f"Client with the earliest check-in date: ")
    clients.get_earliest_checkin_date().show()

    #Latest check-in date
    print(f"Client with the latest check-in date: ")
    clients.get_latest_checkin_date().show()

    #Clients' names alphabetically ordered
    print("\nClients' names ordered alphabetically:")
    for name in clients.get_names():
        print("\t" + name[0] + ", " + name[1])

    #Clients' jobs alphabetically ordered. Does not show a job more than once
    print("\nClients' jobs ordered alphabetically:")
    for job in clients.get_jobs():
        print("\t" + job)

if __name__ == '__main__':
    main()
