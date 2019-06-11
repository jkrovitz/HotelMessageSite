/**
This file contains the functions that more specifically are responsible 
for getting the values from the drop-down lists, set the greeting based 
on the value selected from the greeting drop-down, and then output 
the message that corresponds with the particular greeting.  
**/

function getInputAndConditionalsForOutput() {

  var checkInMessage = ''; 
  var checkOutMessage = ''; 
  var otherMessage = ''; 

  var greetingSelector =  document.getElementById("greetingDropdown").value;
  
  var companyDict = stringToDictionary(document.getElementById("companyDropdown").value); 
  var guestDict = stringToDictionary(document.getElementById("guestDropdown").value);

  if (greetingSelector === 'Check in'){
    divVisibility('displayCheckinMessage');
    outputCheckinMessage(guestDict, companyDict);
  }

  else if(greetingSelector === 'Check out'){
    divVisibility('displayCheckoutMessage');
    outputCheckoutMessage(guestDict, companyDict); 
  }

  else if(greetingSelector === 'More Towels'){
    divVisibility('displayMoreTowelsMessage');
    outputMoreTowelsMessage(guestDict, companyDict);
  }

  //This is the case where a user types a custom message into the select dropdown. 
  else{
     divVisibility('displayOtherMessage');
    $("#greetingDropdown").select2({
      tags: true
    });
    otherMessage = document.getElementById('displayOtherMessage').innerHTML = greetingSelector;
    moreTowelsMessage = document.getElementById('displayMoreTowelsMessage').innerHTML = '';
    checkInMessage = document.getElementById('displayCheckinMessage').innerHTML = '';
    checkOutMessage = document.getElementById('displayCheckoutMessage').innerHTML = ''; 
  }
}


/**
The functions outputCheckinMessage, outputCheckoutMessage, and outputMoreTowelsMessage
all  output messages based on the greeting selcted. 
**/ 

function outputCheckinMessage(guestDict, companyDict){
    return document.getElementById('displayCheckinMessage').innerHTML = 'Good ' 
    + getGreetingTime(parseInt(guestDict.startTimestamp), companyDict.timezone) +
    " " + guestDict.name + ' and welcome to ' +  companyDict.company + '! Room ' + 
    parseInt(guestDict.roomNumber) + 
    ' is now ready for you. Enjoy your stay and let us know if you need anything.' ;
}


function outputCheckoutMessage(guestDict, companyDict){
  return document.getElementById('displayCheckoutMessage').innerHTML = 
    'Good ' + getGreetingTime(parseInt(guestDict.endTimestamp), companyDict.timezone) 
    + " " + guestDict.name + '! Thank you for staying at ' 
    + companyDict.company + 
    '. We wish you safe travels and hope you stay with us again soon.';
}

function outputMoreTowelsMessage(guestDict, companyDict){
  return document.getElementById('displayMoreTowelsMessage').innerHTML = 
    guestDict.name 
    + ', we have notified housekeeping, and they will be bringing some more towels to room ' 
    + parseInt(guestDict.roomNumber) 
    + ' very shortly. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &ndash; ' 
    + companyDict.company + " staff";
}



var divs = ["displayCheckinMessage", "displayCheckoutMessage", "displayMoreTowelsMessage", "displayOtherMessage"];
var visibleDivId = null;

/** Sets the div selected to be the visible div and then calls the function
hideUnselectedOptions **/
function divVisibility(divId) {
    visibleDivId = divId;
    hideUnselectedOptions();
}

/**This functions takes the divs corresponding with the values of the greeting 
options that were not selected and hides them.**/
function hideUnselectedOptions() {
  var i, divId, div;
  for(i = 0; i < divs.length; i++) {
    divId = divs[i];
    div = document.getElementById(divId);
    if(visibleDivId === divId) {
      div.style.display = "block";
    } else {
      div.style.display = "none";
    }
  }
}
