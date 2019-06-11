'''
This file creates objects, passes the properties associated with the object to the function that will 
create a dictionary, and then appends the object to a list specific to the object. 
'''

from hotelMessageClasses.TheClasses.Guest import Guest
from hotelMessageClasses.TheClasses.Company import Company

class AnotherObjectInstance:

	''' The function creates an empty Guest list, creates several Guest objects, creates 
	a dictionary for each object using the object properties for the dictionary values 
	and appending each dictionary to the Guest list.''' 
	def addMoreGuests(self):
		moreGuests = []

		rachel = Guest(7, "Rachel", "Green", "reservation", 123, 1558823732000, 1558945404000)
		monica = Guest(8, "Monica", "Geller", "reservation", 831,1558808731000, 1558959763000)
		phoebe = Guest(9, "Phoebe", "Buffay", "reservation", 613,1558798236000, 1558957503000)
		joey = Guest(10, "Joey", "Tribbiani", "reservation", 444,1574462132000, 1574615846000)
		
		rachelDict = rachel.makeDict("id", 7, "firstName", "Rachel", "lastName", "Green", "reservation", "roomNumber", 123, "startTimestamp", 1558823732000, "endTimestamp", 1558945404000)
		monicaDict = monica.makeDict("id", 8, "firstName", "Monica", "lastName", "Geller", "reservation", "roomNumber", 831, "startTimestamp", 1558808731000, "endTimestamp",1558959763000)
		phoebeDict = phoebe.makeDict("id", 9, "firstName", "Phoebe", "lastName", "Buffay", "reservation", "roomNumber", 613, "startTimestamp", 1558798236000, "endTimestamp", 1558957503000)
		joeyDict = joey.makeDict("id", 10, "firstName", "Joey", "lastName", "Tribbiani", "reservation", "roomNumber", 444, "startTimestamp", 1558823732000, "endTimestamp", 1574615846000)

		moreGuests.append(rachelDict)
		moreGuests.append(monicaDict)
		moreGuests.append(phoebeDict)
		moreGuests.append(joeyDict)
		
		return moreGuests

	''' The function creates an empty Company list, creates several Company objects, creates 
	a dictionary for each object using the object properties for the dictionary values 
	and appending each dictionary to the Company list.''' 
	def addMoreCompanies(self):
		moreCompanies = []

		laVilla126 = Company(6, "La Villa 126", "Dakar", "Africa/Dakar")
		hotelDeFrance = Company(7, "Hotel de France", "Paris", "Europe/Paris")
		
		LaVilla126_dict = laVilla126.makeCompanyDict("id", 6, "company", "La Villa 126", "city", "Dakar", "timezone", "Africa/Dakar")
		hotelDeFrance_dict = hotelDeFrance.makeCompanyDict("id", 7, "company", "Hotel de France", "city", "Paris", "timezone", "Europe/Paris" )

		moreCompanies.append(LaVilla126_dict)
		moreCompanies.append(hotelDeFrance_dict)

		return moreCompanies
		