




let dropdown = document.getElementById('country');
dropdown.length = 0;

let defaultOption = document.createElement('option');
defaultOption.text = 'Choose country';

dropdown.add(defaultOption);
dropdown.selectedIndex = 0;
let cb = function (data)
{
 
    for (d of data) {
      option = document.createElement('option');
      option.text = d.name;
      option.value = d.code;
      dropdown.add(option);
    }
   } 