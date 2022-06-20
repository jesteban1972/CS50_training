# file customerClient: this file uses methods of class Customer
from Customer import Customer

myCustomer = Customer(1, 'Javier')
print('customer id: ' + str(myCustomer.id) + '; customer name: ' + myCustomer.name)