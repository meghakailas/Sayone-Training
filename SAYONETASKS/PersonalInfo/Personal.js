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
      option.value = data[i].abbreviation;
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