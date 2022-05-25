var i=0;
var time=3000;
var images=[];
images[0]='images/2635-ee82a8c79b622dcb1025e1e2ebfbf0d4.png';
images[1]='images/eastern-europe-2.png';
images[2]='images/PTI03-09-2020_000159B.jpg';
function slideshow() {
	document.getElementById('slide').src=images[i];
	if(i<images.length-1){
		i++;
	}
	else{
		i=0;
	}
	setTimeout("slideshow()",time);
}


function forward(){
	if(i<images.length-1){
		i++;
	}
	else{
		i=0;
	}
document.getElementById('slide').src=images[i];
}

function backward(){
	if(i==0){
		i=images.length-1;
	}
	else{i--;}
document.getElementById('slide').src=images[i];
}

window.onload=slideshow;

function Appear()
{
	Resize();
	var e = document.getElementById('news');
       if(e.style.display == 'block')
	   {
			e.style.display = 'none';
			document.getElementById('show').style.marginLeft='17%';
			document.getElementById('in').style.marginLeft='0%';
	   }
         
       else
	   {
			e.style.display = 'block';
			document.getElementById('show').style.marginLeft='5%';
	   }
         
}
function Resize()
{
	document.getElementById('show').style.marginLeft='35%';

}



