function validate(){

			var regEx=/^\+91([6-9])([0-9]){9}$/;
			var namep=document.getElementById("name").value;
			var mailp=document.getElementById("mail").value;
			var agep=document.getElementById("age").value;
			var phno=document.getElementById("numb").value;
		
	if (namep ==""){
			alert("Name required!!");	
		}
	else{	
        	if(mailp== ""){
          	alert("Enter Mailid");
      		}
      		else{
      				if(agep>110 || agep<=0 || agep==" "){
          			alert("Invalid age");
      				}

      				else{
      			 			if ( (phno!="")   &&  (regEx.test(phno)==false) ) {
        
          					alert("Invalid phonenumber");
        					}
        					else{alert("Success!!");}
        				
        			}	

        		}
      
      
		}

}

			
		
		





	


