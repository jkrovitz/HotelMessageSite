#Create a class named Company. 
class Company:

	#Use the __init__() function to asign values for id, company, city, and timezone. 
    def __init__(self, id, company, city, timezone):
        self.id = id
        self.company = company
        self.city = city
        self.timezone = timezone 

    #Create a dictionary with key, value pairs associated with properties of the Company class.
    @staticmethod 
    def makeCompanyDict(idKey, idVal, companyKey, companyVal, cityKey, cityVal, timezoneKey, timezoneVal):
        companyDict = { idKey:idVal, companyKey:companyVal, cityKey: cityVal, timezoneKey:timezoneVal} 
        return companyDict