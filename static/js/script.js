window.onload=function(){
	//client side code for checking the cureent location of the user
	var src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAib7xdoZiu7fUXkuVd3ARsdaAXyrdAyDU&callback=initMap";
	//store state location
	const myCurrentState = 'Lagos';
	const myApiCall = $.getJSON("https://api.openweathermap.org/data/2.5/weather?q=" + myCurrentState + "&appid=cb024eec4cf078a0a96f1eac0907e001",function(data){
        let temp = "The temperature in " + myCurrentState + " is " + data.main.temp + "K" + "<br>";
        let humi = "The humidty in " + myCurrentState + " is " + data.main.humidity + "<br>";
        let wind = "The windspeed in " + myCurrentState + " is " + data.wind.speed + "<br>";
        let weather = "therefore be sure to expect " + data.weather[0].description + "<br>";
        $(".temp").append(temp);
        $(".humidity").append(humi);
        $(".windSpeed").append(wind);
        $(".weatherCondition").append(weather);
		console.log(myApiCall)
		console.log(data.name)
		if (myCurrentState !== data.name){
			alert('sorry lagosians cannot be accessed in your current location')
			document.querySelector('body').innerHTML = '<p>sorry lagosians cannot be accessed in your current location</p>';
		}
	})
	
	changeLikeToUnlike();
 
}

//increment the like,followers list on the client side

//get access to the the like button

function changeLikeToUnlike(){
	//get access to the the like button
	buttonLike = document.querySelector('#like');
	buttonLike.addEventListener('click', function(e){
		console.log('liked');
		this.innerHTML = 'Unlike'

	})
}
