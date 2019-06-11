import json 
from flask import Flask, render_template
from hotelMessageClasses.AnotherObjectInstance import AnotherObjectInstance


app = Flask(__name__)

""" This function is for displaying the home route. A list is created with three JSON files. 
The JSON files are read in and parsed into a list of lists. A variable is assigned to each of the indices 
within the list. Each of the lists are then passed to the home.html template."""
@app.route("/")
@app.route("/home", methods = ['POST', 'GET'])
def home():
	my_json_file_list = ['static/json/Greetings.json', 'static/json/Companies.json', 'static/json/Guests.json']
	hotel_message_site_objects = read_json_files(my_json_file_list)
	hotel_message_site_objects_parse = combineInstances(hotel_message_site_objects)
	greetingList = hotel_message_site_objects_parse[0]
	companyList = hotel_message_site_objects_parse[1]
	guestList = hotel_message_site_objects_parse[2]
	return render_template("home.html", guestList=guestList, companyList=companyList, greetingList = greetingList)

""" This function reads in json_files and parses each file into 
a python object which is then appended to python_objects_list
and returned."""
def read_json_files(json_files):
	python_objects_list = []
	for a_json_file in json_files:
		with open(a_json_file, 'r') as myfile:
			data=myfile.read()
		python_object = json.loads(data)
		python_objects_list.append(python_object)
	return python_objects_list

"""This function takes each of the lists that were parsed from
the JSON file and combines them with the corresponding 
Python object instances."""
def combineInstances(mess_objs):
	list_of_python_obj_lists = []
	greetingList = mess_objs[0]
	companyList = []
	companyList = mess_objs[1] + AnotherObjectInstance().addMoreCompanies()
	guestList = []
	guestList = mess_objs[2] + AnotherObjectInstance().addMoreGuests()
	list_of_python_obj_lists.append(greetingList)
	list_of_python_obj_lists.append(companyList)
	list_of_python_obj_lists.append(guestList)
	return list_of_python_obj_lists


if __name__ == '__main__':
	app.run(debug=True)

