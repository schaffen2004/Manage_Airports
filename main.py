class Airport:
    def __init__(self, id, x, y, its_type):
        self.id = id
        self.x = x
        self.y = y
        self.its_type = its_type


class AirportManager:
    def __init__(self):
        self.airports = {}
        self.flights = []
        self.numberOfAirport = 0

    def addAirport(self, airport):
        if airport.id in self.airports.keys():
            return -1
        self.airports[airport.id] = {'x': airport.x, 'y': airport.y, 'its_type': airport.its_type,
                                     'index': self.numberOfAirport}
        for i in range(0, self.numberOfAirport):
            self.flights[i].append(-1)
        self.numberOfAirport += 1
        self.flights.append([-1] * self.numberOfAirport)
        return self.numberOfAirport - 1

    def addFlight(self, src: str, dest: str, its_types, time, cost):
        if src not in self.airports.keys() or dest not in self.airports.keys():
            return -1
        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        self.flights[indexSrc][indexDest] = [time, cost, its_types]
        self.flights[indexDest][indexSrc] = [time, cost, its_types]

    def showAllAirports(self):
        if len(self.airports) == 0:
            print("Don't have any airport!")
            return -1
        print('--------------------------------All airport information-------------------------------')
        for i in self.airports:
            print(
                f'ID: {i}, Location: {self.airports[i]["x"], self.airports[i]["y"]}, Type: {self.airports[i]["its_type"]}')
        print('--------------------------------------------------------------------------------------')


manager = AirportManager()
airport1 = Airport('1', 20, 11, 'L')
airport2 = Airport('2', 100, 100, 'M')
manager.addAirport(airport1)
manager.addAirport(airport2)
manager.addFlight('1', '2', 'L', 60, 100)
print(manager.flights)
manager.showAllAirports()
