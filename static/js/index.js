/**
This file has a function that calls the select2 library, a function that 
handles the submission of the form to get the message output, 
a function called stringToDictionary, and another 
function called getGreetingTime. 
**/


/**As soon as the page loads, this function 
allows a user to dynamically create 
a new message/greeting based on text 
input by the user. **/
$(document).ready(function() {
  $("#greetingDropdown").select2({
    tags: true
  });
   /**this hides the box so a user is not able to enter a custom value. 
   Select2 is used for the drop-down list of companies and the drop-down
   list of guests in order to keep the formatting of the 3 drop-down 
   lists consistent.**/
   $('#companyDropdown').select2({
    minimumResultsForSearch: -1
  });
   $('#guestDropdown').select2({
    minimumResultsForSearch: -1
  });
 });

/**In this event method, when the form is submitted, the 
event calls preventDefault, which prevents the page
from being reloaded when it is submitted. After this, 
the function showInput is called. **/
$('#myform').submit( function(e) {
  e.preventDefault();
  getInputAndConditionalsForOutput(); 
});

/* Converts the string value of the  option
 that is selected in each drop-down
list to a dictionary.  */
function stringToDictionary(selectOptionString) {
  var dictionary = {};
  if (selectOptionString.indexOf('?') === 0) {
    selectOptionString = selectOptionString.substr(1);
  }
  var parts = selectOptionString.split('&');
  for(var i = 0; i < parts.length; i++) {
    var p = parts[i];
    var keyValuePair = p.split('=');
    var key = keyValuePair[0];
    var value = keyValuePair[1];
    dictionary[key] = value;
    value = decodeURIComponent(value);
    value = value.replace(/\+/g, ' ');
  }
  return dictionary;
}

/** The function takes in startTimestamp and endTimestamp
in milliseconds and uses Moment.js to convert it into 
hours. It then returns whether the hours are in the 
morning, afternoon, or evening in order to display
the correct greeting.**/
function getGreetingTime (milseconds,  tZone) {
  var g = null; 
  date = new Date(milseconds);
  var split_afternoon = 12 
  var split_evening = 16   
  var theTime = moment(milseconds);
  var currentHour = theTime.tz(tZone).format('HH');
  if(currentHour >= split_afternoon && currentHour <= split_evening) {
    g = "afternoon";
  } else if(currentHour > split_evening) {
    g = "evening";
  } else {
    g = "morning";
  }
  return g;
}
