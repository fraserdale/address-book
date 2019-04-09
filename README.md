# address-book
An address book with the specification:  
* Your address book should list organisations and people.  
* It should allow the user to see the names and contact details of people in organisations, and to manage the people who are in an organisation.  
* It should store a name and contact details for each organisation.  
* Your address book should allow organisations and people to be created, edited and deleted.

## Solution
This solution uses the pymongo module and an mlab database to store the information about the organisations and their employees.  
The solution is written using python3 backend which is bound to the HTML front end using flask.  
The lists are sorted by name (ascending)

## Instructions
Using python3   
Download/Clone the repository  
Please insert the database login password I have given you in the email in line 8 of `start.py` like below
![Set Password](https://github.com/fraserdale/address-book/blob/master/images/password_insert.gif "Set Password")  
Run `python start.py`  
This will serve the app on `127.0.0.1:3000`  

### Demonstration Gifs
On the home page you can add/edit/delete organisations
1. Create Organisation  
![Create Organisation](https://github.com/fraserdale/address-book/blob/master/images/add_org.gif "Create Organisation")   
2. Edit Organisation  
![Edit Organisation](https://github.com/fraserdale/address-book/blob/master/images/change_org.gif "Edit Organisation")   
3. Delete Organisation  
![Delete Organisation](https://github.com/fraserdale/address-book/blob/master/images/delete_org.gif "Delete Organisation")   

On each organisation page you can edit or delete the organisation and add/edit/delete employees
1. Edit Organisation  
![Edit Organisation](https://github.com/fraserdale/address-book/blob/master/images/change_org.gif "Edit Organisation")   
2. Add Employee 
![New Employee ](https://github.com/fraserdale/address-book/blob/master/images/new_emp.gif "New Employee")   
3. Edit Employee  
![Edit Employee ](https://github.com/fraserdale/address-book/blob/master/images/edit_emp.gif "Edit Employee")   
