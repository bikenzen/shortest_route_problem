from collections import defaultdict, namedtuple

class City:
    '''City that has airport.'''

    def __init__(self, name):
        self.name = name
        self.flights = defaultdict(self.factory) # {city: (price, route)}
        self.checked = False

    def add_flight(self, another, price):
        self.flights[another].price = price

    def __repr__(self):
        return "<City {}>".format(self.name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    @staticmethod
    def factory():
        flight = namedtuple("Flight", ["price", "route"])
        flight.price = 0
        flight.route = []
        return flight

city_names = ["Atlanta", "Boston", "Chicago", "Denver", "El Paso"]
for city_name in city_names:
    exec("{} = City('{}')".format(city_name.lower().replace(" ", "_"), city_name))

atlanta.add_flight(denver, 160)
atlanta.add_flight(boston, 100)

boston.add_flight(chicago, 120)
boston.add_flight(denver, 10)

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
        new_price = cheap_flights[current_city].price + current_city.flights[neighbor].price
        if cheap_flights[neighbor].price == 0 or new_price < cheap_flights[neighbor].price:
            cheap_flights[neighbor].price = new_price
            cheap_flights[neighbor].route = cheap_flights[current_city].route.copy()
            cheap_flights[neighbor].route.append(current_city)

    unvisited = dict(filter(lambda c: not c[0].checked, cheap_flights.items()))
    if (len(unvisited)):
        next_cheapest_city = min(unvisited.items(), key=lambda f: f[1].price)[0]
        check_city(next_cheapest_city, cheap_flights)

cheap_flights = defaultdict(City.factory)
cheap_flights.update(atlanta.flights)

check_city(atlanta, cheap_flights)

for city, flight in cheap_flights.items():
    print("To", city.name)
    print("Price: ", flight.price)
    print("Route: ", ", ".join(city.name for city in flight.route))
    print()
