# address-book
* An address book with the specification:  
* Your address book should list organisations and people.  
* It should allow the user to see the names and contact details of people in organisations, and to manage the people who are in an organisation.  
* It should store a name and contact details for each organisation.  
* Your address book should allow organisations and people to be created, edited and deleted.

## Solution
This solution uses the pymongo module and an mlab database to store the information about the organisations and their employees.  
The solution is written using python3 backend which is bound to the HTML front end using flask.

## Instructions
Using python3  
Download/Clone the repository and run `python start.py`  
This will serve the app on 1127.0.0.1:30001

### Demonstration Images
1. On the home page you can add/edit/delete organisations
![Address Book Home](https://github.com/fraserdale/address-book/blob/master/images/address_book_home.PNG "Address Book Home")
2. On the organisation page you can edit/delete the organisation and add/edit/delete employees
![Organisation Page](https://github.com/fraserdale/address-book/blob/master/images/organisation_page.PNG "Organisation Page")
3. On the employee page you can edit/delete the employee
![Employee Page](https://github.com/fraserdale/address-book/blob/master/images/employee_page.PNG "Employee Page")
