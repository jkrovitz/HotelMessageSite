# HotelMessage Site

## Instructions for running the program

1. Install Python 3 if it is not installed already

2. Open the terminal / command prompt. 

3. Change the directory to be the absolute path to where the repository folder is located. 

	+ i.e. **cd /Users/jkrovitz/DocumentsJeremyMacBookPro/git/HotelGreetingSite**

4. Install Flask. You can do a pip install. 

5. Then type **python3 greetings.py**. 

	+ If the program does not open in an internet browser window as expected, the destination address for the program is **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

6. You then choose a value in each of the select boxes, click `<submit>`, and a message will be output. 

*To output a custom message, type the input into the top most select box (the select box with the heading "Choose the Message") and press `<return>`. When you hit submit, your custom message will be displayed. The bottom two select boxes will not output any text, if you have typed a custom message into the top select box.*

## Design decisions overview
I used three select option drop-down boxes, so that the user of the program would be able to select the greeting, the company, and the guest that gets loaded in from the JSON file.

I wanted to be sure that I throughoughly considered edge cases when writing the code. For 
this reason, I had to be sure I added additional instances of the objects. I felt that it was important not to modify the JSON files provided to me, but rather create a Python class for both Guest (created in the file Guest.py) and Company (created in the file Company.py), create several instances of each of the classes, put them in 
lists, and then combine the lists

## Languages picked and why
I used the Python framework flask, so that I could load in the JSON files convert them to python objects, assign the python objects to variables, and then pass the variables to the Jinja template engine, which allowed me to access each variable's attributes in index.html. The benefit of this approach was that I was able to concatenate several variable properties for each option value, which I then passed to the function called stringToDictionary, which does as it says, converts the option value string to JS dictionary. Having a JS dictionary makes it possible to access multiple object properties in JavaScript as Jinja syntax cannot be used direclty in JavaScript. The JS dictionary made it possible to access the individual properties like Guest.firstName, and Guest.reservation.roomNumber and be able to them in several places within the larger string. Otherwise one property would have needed to come directly after the other. 

When considering how I was going to approach this project, I considered making ajax calls 
or somehow reading the JSON files directly in JavaScript. For client-side JavaScript the files would need to be be hosted on the Internet. I felt that since I was provided the JSON files locally, they should be loaded locally. Python allowed me to do this. 


## Process for verifying the correctness of program
I created more json objects in both Companies.json and Guests.json. For the companies, I made the timezones more different to ensure that the JavaScript function getGreetingTime was working properly and would very the greeting based on the timezone. Similarly, I created four additional guests and made sure that the times of day they checked in/out varied to make sure that the correct greeting would be output. 


| [![Test1](https://raw.githubusercontent.com/jkrovitz/HotelMessageSite/master/static/imagesOfTests/JoeyTribbianiTheGrandBudapestHotelCheckin.png)](https://raw.githubusercontent.com/jkrovitz/HotelMessageSite/master/static/imagesOfTests/JoeyTribbianiTheGrandBudapestHotelCheckin.png)  | [![Test2](https://raw.githubusercontent.com/jkrovitz/HotelMessageSite/master/static/imagesOfTests/PhoebeBuffayLaVilla126CheckOut.png?raw=true)](https://raw.githubusercontent.com/jkrovitz/HotelMessageSite/master/static/imagesOfTests/PhoebeBuffayLaVilla126CheckOut.png?raw=true) | 
|:---:|:---:|
| Joey Tribbiani, Check in, Evening greeting, The Grand Budapest Hotel, US/Central timezone | Phoebe Buffay, Check out, Morning greeting, La Villa 126, Africa/Dakar timezone  

## What I might do if I had more time 
If I had more time, I would create a database and add the data from the three JSON files to a database. A database would be beneficial to store information about each of the users of the Hotel Message Site such as their email, username, and password. A database would have also provided the functionality to check whether there would be a conflict assigning a certain guest, such as if one guest already had the room. If I were to add a database, I would probably use MongoDB, which I don't have as much exposure to, but I want to gain more exposure to it. MongoDB is a NoSQL database, which is advantageous in this case because it makes object oriented programming easier to implement since it is more horizontally scalable. Furthermore, I would also add more greetings and create two diffferent views - a view for guests and a view for hotel employees. I would create a login system and have the database keep track of each user and specify whether it was a guest or employee. I would have also have created additional messages. 
