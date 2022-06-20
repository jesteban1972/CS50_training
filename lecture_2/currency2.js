document.addEventListener('DOMContentLoaded', function() {
	
	document.querySelector('form').onsubmit = function() {
		var headers = new Headers();
		headers.append("apikey", "AVdPqlps4CiKURMUWwwQMHU9fhWBNGn3");
	
		var request = {
			method: 'GET',
			redirect: 'follow',
			headers: headers
		};
		
		const currency = document.querySelector('#currency').value.toUpperCase();
	
		fetch('https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=' + currency + '&amount=1', request)
		.then(response => response.json())
		.then(data => {
			const rate = data.result;
			
			if (rate !== undefined) {
				document.querySelector('#result').innerHTML = `1 ${currency} is equal to ${rate.toFixed(3)} EUR.`;
			} else {
				document.querySelector('#result').innerHTML = 'Invalid Currency.';
			}
		})
		.catch(error => console.log('Error:' , error));
		
		return false;
	};	
});