
var timeInt;

function auto(){
	timeInt=setInterval(onlyRed,1000);
	onlyRed();
}

function onlyRed(){
	if ((red.style.fill=="black") &&  (yellow.style.fill=="black")){
		red.style.fill="red";
		yellow.style.fill="black";
		green.style.fill="black";

	}else if(red.style.fill=="red"){
	onlyYellow();

	}
	else if (yellow.style.fill=="yellow"){
		onlyGreen();
	}
}

function onlyYellow(){
	if(yellow.style.fill== "black" ){
		yellow.style.fill="yellow";
		red.style.fill="black";
	}

}

function onlyGreen(){
	if (green.style.fill=="black"){
		green.style.fill="green";
		yellow.style.fill="black";
	}
}
 function stop(){
 	clearInterval(timeInt);
 	red.style.fill="black";
 	yellow.style.fill="black";
 	green.style.fill="black";
 }

 function blinkYellow(){
 	timeInt=setInterval(bYellow,500);
 		bYellow();
 
 }
 function bYellow(){
 	if (yellow.style.fill=="black"){
 		yellow.style.fill="yellow";
 		red.style.fill="black";
 		green.style.fill="black";
 	}
 	else{
 		yellow.style.fill="black";
 	}
 }