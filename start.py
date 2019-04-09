# Name: Fraser Dale
# Email: fraserdale2@gmail.com
# Date: 09/04/19
# Instuctions: Run this file (start.py) and navigate to 127.0.0.1:3000 or localhost:3000

# Please insert password specified in email here!!!
# If there is an issue please email me: fraserdale2@gmail.com
password = ' '

# The rest of the program does to require to be changed.


import pymongo
from bson import ObjectId
from flask import Flask,render_template,request,redirect

#setup flask app
app = Flask(__name__)

# Mongo client connection
try:
	MONGODB_URI = "mongodb://fraser:"+ password +"@ds135036.mlab.com:35036/address-book"
	mongo_client = pymongo.MongoClient(MONGODB_URI, connectTimeoutMS=30000)
	# Select address-book database and initialise the organisations and employees collections
	db = mongo_client.get_database("address-book")
	organisations = db.organisations
	employees = db.employees
except:
	print('Error connecting to database, missing part of MONGODB_URI')
	quit()



# home index route, returns all the organisations, names and contact details.
@app.route("/",methods=['GET'])
def home():
	organisationsDump = organisations.find({}).sort([("name",pymongo.ASCENDING)])
	return render_template('index.html',organisations=organisationsDump)

# create new organisation, inserts name and contact details
# from post request into organisation collection then redirects
@app.route('/organisation',methods=['POST'])
def newOrganisation():
	request_information = request.form
	organisations.insert({
		"name": request_information['name'],
		"contact": request_information['contact']
	})
	return redirect("/", code=302)

# recieves get request, based on query string ID parameter returns
# different organisation information
@app.route('/organisation',methods=['GET'])
def getOrganisation():
	# error handling if no id is provided
	if request.args.get('id') == None:
		return redirect("/", code=302)
	organisation_id = request.args.get('id')
	organisation = organisations.find_one({"_id": ObjectId(organisation_id)})
	employeesDump = employees.find({"organisationID": organisation_id}).sort([("name",pymongo.ASCENDING)])
	return render_template('organisation.html', organisation=organisation, employees=employeesDump)

# updates the information about the organisation
# based on the parameters given in post form data
@app.route('/updateOrganisation',methods=['POST'])
def updateOrganisation():
	request_information = request.form
	organisations.update_one({'_id': ObjectId(request_information['id'])}, {
			'$set': {"name":request_information['name'],"contact":request_information['contact']}
		}, upsert=False)
	organisation_id = request_information['id']
	organisation = organisations.find_one({"_id": ObjectId(organisation_id)})
	employeesDump = employees.find({"organisationID":organisation_id}).sort([("name",pymongo.ASCENDING)])
	return render_template('organisation.html', organisation=organisation,employees=employeesDump)

# deletes the organisation specified
# deletes all the employees that belong to the company
@app.route('/deleteOrganisation',methods=['POST'])
def deleteOrganisation():
	request_information = request.form
	organisations.delete_one({"_id": ObjectId(request_information['id'])})
	employees.delete_many({"organisationID":request_information['id']})
	organisationsDump = organisations.find({}).sort([("name",pymongo.ASCENDING)])
	return render_template('index.html',organisations=organisationsDump)

# employee page displays name and contact information about
# the employee specified in querystring
@app.route('/employee',methods=['GET'])
def getEmployee():
	#error handling if no id is provided
	if request.args.get('id') == None:
		return redirect("/", code=302)
	employee_id = request.args.get('id')
	employee = employees.find_one({"_id": ObjectId(employee_id)})
	organisation = organisations.find_one({"_id": ObjectId(employee['organisationID'])})
	return render_template('employee.html', organisation=organisation, employee=employee)

# inserts employee into the employees collection
# based on info submitted in post request
@app.route('/addEmployee',methods=['POST'])
def addEmployee():
	request_information = request.form
	employees.insert({"name": request_information['name'], "contact": request_information['contact'],
 					  "organisationID": request_information['id']})
	organisation_id = request_information['id']
	organisation = organisations.find_one({"_id": ObjectId(organisation_id)})
	employeesDump = employees.find({"organisationID":organisation_id}).sort([("name",pymongo.ASCENDING)])
	return render_template('organisation.html', organisation=organisation,employees=employeesDump)

# udpates the information relating to the employee
# specified in the form data
@app.route('/updateEmployee',methods=['POST'])
def updateEmployee():
	request_information = request.form
	employees.update_one({'_id': ObjectId(request_information['id'])}, {
		'$set': {"name": request_information['name'], "contact": request_information['contact']}
	}, upsert=False)
	employee_id = request_information['id']
	employee = employees.find_one({"_id": ObjectId(employee_id)})
	organisation = organisations.find_one({"_id": ObjectId(employee['organisationID'])})
	return render_template('employee.html', organisation=organisation, employee=employee)


# deletes the employee from the collection
@app.route('/deleteEmployee',methods=['POST'])
def deleteEmployee():
	request_information = request.form
	employee = employees.find_one({"_id":ObjectId(request_information['id'])})
	organisation_id = employee['organisationID']
	organisation = organisations.find_one({"_id":ObjectId(organisation_id)})
	employees.delete_one({"_id": ObjectId(request_information['id'])})
	employeesDump = employees.find({"organisationID":organisation_id}).sort([("name",pymongo.ASCENDING)])
	return render_template('organisation.html', organisation=organisation, employees=employeesDump)

# general 404 error handler
@app.errorhandler(404)
def page_not_found(e):
	return render_template('error.html'), 404

if __name__ == "__main__":
	# check DB login is correct
	try:
		db.list_collection_names()
		print('Successfully connected to the database...')
	except:
		print('Unable to login to the database, please ensure password is set correctly on line 8')
		quit()
	# start server
	app.run(port=3000,debug=False)