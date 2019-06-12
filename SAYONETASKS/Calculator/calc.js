


function getVal(obj){
	var inputLabel=document.getElementById("inputVal");
	var pushed=obj.innerHTML;

	if (pushed=="="){
		inputLabel.innerHTML=eval(inputLabel.innerHTML);
	}
	else if(pushed=="CLS"){
		inputLabel.innerHTML='0';

			}
		else{
			if(inputLabel.innerHTML=="0"){
				inputLabel.innerHTML=pushed;

			}
			else{
				inputLabel.innerHTML+=pushed;
			}
		}




}