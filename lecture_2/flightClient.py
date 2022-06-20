from Flight import Flight

capacity = input('input flight capacity: ')
flight = Flight(int(capacity))

print('boarding passengers. input passenger names (blank to finish)')
while(True):
    name = input('passenger: ')
    if name == '':
        break
    if flight.getOpenSeats() > 0:
        flight.addPassenger(name)
    else:
        print(f"No available seats for {name}")

print('boarding finished. passengers boarded:')
for passenger in flight.passengers:
    print(passenger)