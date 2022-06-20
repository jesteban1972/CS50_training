from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Flight, Airport, Passenger

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST": # For a post request, add a new flight
        try:
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) # Finding the passenger based on the id
            flight = Flight.objects.get(pk=flight_id) # Accessing the flight
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        passenger.flights.add(flight) # Add passenger to the flight
        return HttpResponseRedirect(reverse("flight", args=(flight_id,))) # Redirect user to flight page