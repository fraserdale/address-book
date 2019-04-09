import pymongo
from bson import ObjectId
from flask import Flask,render_template,request

app = Flask(__name__)
MONGODB_URI = "mongodb://fraser:Secure_1@ds135036.mlab.com:35036/address-book"
mongo_client = pymongo.MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = mongo_client.get_database("address-book")
organisations = db.organisations
employees = db.employees


@app.route("/",methods=['GET','POST'])
def home():
	if request.method == 'POST':
		request_information = request.form
		organisations.insert({
			"name": request_information['name'],
			"contact": request_information['contact']
		})
	organisationsDump = organisations.find({})
	return render_template('index.html',organisations=organisationsDump)

@app.route('/updateOrganisation',methods=['GET','POST'])
def updateOrganisation():
	if request.method == 'POST':
		request_information = request.form
		organisations.update_one({'_id': ObjectId(request_information['id'])}, {
				'$set': {"name":request_information['name'],"contact":request_information['contact']}
			}, upsert=False)
		organisation_id = request_information['id']
	if request.method == 'GET':
		organisation_id = request.args.get('id')
	organisation = organisations.find_one({"_id": ObjectId(organisation_id)})
	employeesDump = employees.find({"organisationID":organisation_id})
	return render_template('organisation.html', organisation=organisation,employees=employeesDump)

@app.route('/deleteOrganisation',methods=['POST'])
def deleteOrganisation():
	request_information = request.form
	organisations.delete_one({"_id": ObjectId(request_information['id'])})
	employees.delete_many({"organisationID":request_information['id']})
	organisationsDump = organisations.find({})
	return render_template('index.html',organisations=organisationsDump)


@app.route('/addEmployee',methods=['GET','POST'])
def addEmployee():
	if request.method == 'POST':
		request_information = request.form
		employees.insert({"name": request_information['name'], "contact": request_information['contact'],
 						  "organisationID": request_information['id']})
		organisation_id = request_information['id']
	if request.method == 'GET':
		organisation_id = request.args.get('id')
	organisation = organisations.find_one({"_id": ObjectId(organisation_id)})
	employeesDump = employees.find({"organisationID":organisation_id})
	return render_template('organisation.html', organisation=organisation,employees=employeesDump)

@app.route('/updateEmployee',methods=['GET','POST'])
def updateEmployee():
	if request.method == 'POST':
		request_information = request.form
		employees.update_one({'_id': ObjectId(request_information['id'])}, {
			'$set': {"name": request_information['name'], "contact": request_information['contact']}
		}, upsert=False)
		employee_id = request_information['id']
	if request.method == 'GET':
		employee_id = request.args.get('id')
	employee = employees.find_one({"_id": ObjectId(employee_id)})
	organisation = organisations.find_one({"_id": ObjectId(employee['organisationID'])})
	return render_template('employee.html', organisation=organisation, employee=employee)

@app.route('/deleteEmployee',methods=['POST'])
def deleteEmployee():
	request_information = request.form
	employee = employees.find_one({"_id":ObjectId(request_information['id'])})
	organisation_id = employee['organisationID']
	organisation = organisations.find_one({"_id":ObjectId(organisation_id)})
	employees.delete_one({"_id": ObjectId(request_information['id'])})
	employeesDump = employees.find({"organisationID":organisation_id})
	return render_template('organisation.html', organisation=organisation, employees=employeesDump)

if __name__ == "__main__":
	app.run(port=3000)