

function loadDoc(){
  var xHttp = new XMLHttpRequest();
  xHttp.onreadystatechange = function(){
      if (this.readyState == 4 && this.status == 200){
          document.getElementById("bookingCart").innerHTML =this.responseText;
      }
  };
  xHttp.open("GET" , "http://127.0.0.1:8000//details" , true);
  xHttp.send();
}
