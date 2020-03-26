from collections import defaultdict

class City:
    '''City that has airport.'''

    def __init__(self, name):
        self.name = name
        self.flights = defaultdict(int)
        self.checked = False

    def add_flight(self, another, price):
        self.flights[another] = price

    def __repr__(self):
        return "<City {}>".format(self.name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


city_names = ["Atlanta", "Boston", "Chicago", "Denver", "El Paso"]
for city_name in city_names:
    exec("{} = City('{}')".format(city_name.lower().replace(" ", "_"), city_name))

atlanta.add_flight(denver, 160)
atlanta.add_flight(boston, 100)

boston.add_flight(chicago, 120)
boston.add_flight(denver, 120)

chicago.add_flight(el_paso, 80)

denver.add_flight(chicago, 40)
denver.add_flight(el_paso, 140)

el_paso.add_flight(boston, 100)

def check_city(current_city, cheap_flights):
    if current_city.checked:
        return
    else:
        current_city.checked = True

    # update cheap_flights after a new city has been investigated
    for neighbor in current_city.flights:
        new_price = cheap_flights[current_city] + current_city.flights[neighbor]
        if cheap_flights[neighbor] == 0 or new_price < cheap_flights[neighbor]:
            cheap_flights[neighbor] = new_price

    unvisited = dict(filter(lambda c: not c[0].checked, cheap_flights.items()))
    if (len(unvisited)):
        # next_cheapest_city = min(unvisited.items(), key=lambda f: f[1])[0]
        check_city(list(unvisited.items())[0][0], cheap_flights)

cheap_flights = defaultdict(int)
cheap_flights.update(atlanta.flights)

print(cheap_flights)

check_city(atlanta, cheap_flights)
print(cheap_flights)
