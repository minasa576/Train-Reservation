function setVisibility(objectClass, state) {
    var object = document.getElementsByClassName(objectClass);
    for (var i = 0; i < object.length; i++) {
        object[i].style.visibility = state;
      }
    
}
function toggleVisibility(objectID) {
    var object = document.getElementById(objectID);
    state = object.style.visibility;
    if (state == 'visible') object.style.visibility = 'hidden';
    else object.style.visibility = 'visible';
}

function toggleArrow(objectSrc){
    var object = document.getElementById(objectID);
    


}