
function booked(objectID) {
    objectID.style.borderColor = "red";
}
function loadDoc(){
  var xHttp = new XMLHttpRequest();
  xHttp.onreadystatechange = function(){
      if (this.readyState == 4 && this.status == 200){
          document.getElementById("bookingCart").innerHTML =this.responseText;
      }
  };
  xHttp.open("GET" , "details.html" , true);
  xHttp.send();
}
