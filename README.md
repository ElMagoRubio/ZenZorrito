# ZenZorrito
Repository for the evaluation of ZenZorrito's practical evaluation

Steps to take before each commit:

1. Document how CSV files work
   
2. Create a Python module that will contain the functions and classes

3. Create the "Client" class. By doing this, we will be able to manage the retrieved data in a more congruent manner. The Client class will have the following attributes:
   - First Name, Last Name, Street, Zip, City, Type, Job, Phone, Last Check-In Date and Company.
   
4. Create the constructors and destructors for the Client class

5. Create the getters and setters for the Client class

6. Create a "Clients" class, that will contain a list of Client type object to operate with
   
7. Overload the reading operator, so that we can retrieve the Clients data from a CSV file
   
8. Create the necessary methods, such that we can:
   - Retrieve the customer with the earliest check in date.
   - Retrieve the customer with the latest check in date.
   - Retrieve a list of customer’s full names ordered alphabetically.
   - Retrieve a list of the companies user’s jobs ordered alphabetically.

9. Add the necessary exceptions:
   - A required field is empty for that row but the rest of the file is still processed.
   - A row contains less fields than expected but the rest of the file is still processed.
   - A row does not contain any data but the rest of the file is still processed.
