document.addEventListener('DOMContentLoaded', function() {
	
	var headers = new Headers();
	headers.append("apikey", "AVdPqlps4CiKURMUWwwQMHU9fhWBNGn3");
	
	var request = {
		method: 'GET',
		redirect: 'follow',
		headers: headers
	};
	
	// Send a GET request to the URL
    fetch('https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=USD&amount=1', request)
    // Put response into json form
    .then(response => response.json())
	.then(result => {
		const rate = result.result;
		document.querySelector('body').innerHTML = `1 USD is equal to ${rate.toFixed(3)} EUR.`;
	})
	.catch(error => console.log('error' , error));	
});
