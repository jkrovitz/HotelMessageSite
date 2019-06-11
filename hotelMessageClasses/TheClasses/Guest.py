#Create a class named Guest. 
class Guest:

    #Use the __init__() function to asign values for id, firstName, lastName, reservation, roomNumber, reservation_startTimestamp, and reservation_endTimestamp. 
    def __init__(self, id, firstName, lastName, reservation, roomNumber, reservation_startTimestamp, reservation_endTimestamp):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.reservation = reservation
        self.roomNumber = roomNumber
        self.reservation_startTimestamp = reservation_startTimestamp
        self.reservation_endTimestamp = reservation_endTimestamp

    #Create a dictionary with key, value pairs associated with properties of the Guest class.
    @staticmethod 
    def makeDict(idKey, idVal, firstNameKey, firstNameVal, lastNameKey, lastNameVal, reservation_key, roomNumber_key, roomNumber_val , reservation_nested_startTimestamp_key, reservation_nested_startTimestamp_val, reservation_nested_endTimestamp_key, reservation_nested_endTimestamp_val):
        nested_dict = { idKey:idVal, firstNameKey:firstNameVal, lastNameKey: lastNameVal, reservation_key : {roomNumber_key: roomNumber_val, reservation_nested_startTimestamp_key:reservation_nested_startTimestamp_val, reservation_nested_endTimestamp_key:reservation_nested_endTimestamp_val}}
        return nested_dict