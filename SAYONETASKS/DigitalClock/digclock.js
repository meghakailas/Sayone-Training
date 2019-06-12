function showTime(){
        var date= new Date();
        var hour=date.getHours();
        var Minute=date.getMinutes();
        var Second=date.getSeconds();
        var zone="AM"
        if(hour==0){
        hour=12;}
         if(hour>12){
        hour=hour-12;
        zone="PM";}
        if(hour<10)
        {
        hour= "0" + hour;
        }
        if(Minute<10){
        Minute="0"+Minute;
        }
        if(Second<10){
        Minute="0"+Second;
        }
        var time= hour + ":" + Minute + ":" + Second+" " +zone;
        document.getElementById("Clock").innerText =time;

                setTimeout(showTime,1000);
                 }
        showTime()
