var name=document.getElementById("name");
var mailId=document.getElementById("email");
var coun=document.getElementById("country");
var reg=document.getElementById("region");





  
function openRegion(){


let dropregion = document.getElementById('region');
dropregion.length = 0;

let defaultOption = document.createElement('option');
defaultOption.text = 'Choose Region';

dropregion.add(defaultOption);
dropregion.selectedIndex = 0;

let country =document.getElementById('country');

const rl = 'http://battuta.medunes.net/api/region/'+ country.value +'/all/?key=b54c942e0959e98dd9240ad02e7330c1';

const request = new XMLHttpRequest();
request.open('GET', rl, true);

request.onload = function() {
  if (request.status === 200) {
    const data = JSON.parse(request.responseText);
    let option;
    for (let i = 0; i < data.length; i++) {
      option = document.createElement('option');
      option.text = data[i].region;
      option.value = data[i].code;
      dropregion.add(option);
    }
   } else {
    // Reached the server, but it returned an error
  }   
}

request.onerror = function() {
  console.error('An error occurred fetching the JSON from ' + url);
};

request.send();
}


let dropdown = document.getElementById('country');
dropdown.length = 0;

let defaultOption = document.createElement('option');
defaultOption.text = 'Choose Country';

dropdown.add(defaultOption);
dropdown.selectedIndex = 0;

const url = 'http://battuta.medunes.net/api/country/all/?key=b54c942e0959e98dd9240ad02e7330c1';

const request = new XMLHttpRequest();
request.open('GET', url, true);

request.onload = function() {
  if (request.status === 200) {
    const data = JSON.parse(request.responseText);
    let option;
    for (let i = 0; i < data.length; i++) {
      option = document.createElement('option');
      option.text = data[i].name;
      option.value = data[i].code;
      dropdown.add(option);
    }
   } else {
    // Reached the server, but it returned an error
  }   
}

request.onerror = function() {
  console.error('An error occurred fetching the JSON from ' + url);
};

request.send();

function registration(){
  if ((name =="") || (mailId=="") ||(coun.value=="")||(reg.value=="") )
  {alert("Enter details");}
  else if(coun.value=="" || reg.value=="" ){
    alert("Select Country/Region");
  }
  else{alert("Success!!!");}
}