import client
import csv
import os

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
        return 0
    
    def get_latest_checkin_date(self):
        return 0
    
    def get_names(self):
        return 0

    def get_jobs(self):
        return 0
    
    #This function is used to properly print all the clients in the list, using client.show()
    def show(self):
        for client in self.client_list:
            client.show()


# Obtén la ruta al directorio actual donde se encuentra el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta al archivo CSV a partir del directorio del script
csv_file = os.path.join(script_dir, '../data/sample.csv')

# Crea una instancia de Clients con la ruta al archivo CSV
clients = Clients(csv_file)