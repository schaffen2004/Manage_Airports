import sys


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
        self.types = {'S': 1, 'M': 2, 'L': 3}

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
        if self.types[its_types] > self.types[self.airports[src]['its_type']] or self.types[its_types] > self.types[
            self.airports[dest]['its_type']]:
            return -1
        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        self.flights[indexSrc][indexDest] = [src, dest, time, cost, its_types]
        self.flights[indexDest][indexSrc] = [dest, src, time, cost, its_types]

    def updateAirport(self, airport):
        if airport.id not in self.airports.keys():
            return -1
        self.airports[airport.id] = {'x': airport.x, 'y': airport.y, 'its_type': airport.its_type,
                                     'index': self.airports[airport.id]['index']}

    def updateFlight(self, src: str, dest: str, its_types, time, cost):
        if src not in self.airports.keys() or dest not in self.airports.keys():
            return -1
        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        print(indexSrc, indexDest)
        self.flights[indexSrc][indexDest] = [src, dest, time, cost, its_types]
        self.flights[indexDest][indexSrc] = [dest, src, time, cost, its_types]

    def deleteFlight(self, src: str, dest: str):
        if src not in self.airports.keys() or dest not in self.airports.keys():
            return -1
        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        self.flights[indexSrc][indexDest] = -1
        self.flights[indexDest][indexSrc] = -1

    def deleteAirport(self, id):
        if id not in self.airports.keys():
            return -1
        temp = self.airports[id]['index']
        for i in range(0, self.numberOfAirport):
            self.flights[i].pop(temp)
        self.flights.pop(temp)
        self.airports.pop(id)
        for i in self.airports.keys():
            self.airports[i]['index'] -= 1
        self.numberOfAirport -= 1

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1
        for u in range(self.numberOfAirport):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    def findShortestPath(self, src: str, dest: str, mode: int):
        if src not in self.airports.keys() or dest not in self.airports.keys():
            return -1, []
        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        dist = [sys.maxsize] * self.numberOfAirport
        dist[indexSrc] = 0
        sptSet = [False] * self.numberOfAirport
        path = [-1] * self.numberOfAirport
        for cout in range(self.numberOfAirport):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.numberOfAirport):
                if self.flights[x][y] == -1:
                    continue
                if self.flights[x][y][mode] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.flights[x][y][mode]:
                    dist[y] = dist[x] + self.flights[x][y][mode]
                    path[y] = x
        shortest_path = []
        current = indexDest
        while current != -1:
            shortest_path.append(current)
            current = path[current]
        shortest_path.reverse()

        return dist[indexDest], shortest_path

    def showAllAirports(self):
        if len(self.airports) == 0:
            print("Don't have any airport!")
            return -1
        print('--------------------------------All Airport Information-------------------------------')
        for i in self.airports:
            print(
                f'ID: {i}, Location: {self.airports[i]["x"], self.airports[i]["y"]}, Type: {self.airports[i]["its_type"]}')
        print('--------------------------------------------------------------------------------------')

    def showAllFlights(self):
        if self.numberOfAirport == 0:
            print("No flights")
            return
        count = 0
        print('--------------------------------All Flight Information--------------------------------')
        for i in range(len(self.flights)):
            for j in range(len(self.flights[i])):
                if i != j and self.flights[i][j] != -1:
                    count += 1
                    print(
                        f'From:{self.flights[i][j][0]}, To: {self.flights[i][j][1]}, Time: {self.flights[i][j][2]}, Cost: {self.flights[i][j][3]}, Airplane type: {self.flights[i][j][4]}')
        if count == 0:
            print("No flights")
        print('---------------------------------------------------------------------------------------')


manager = AirportManager()
airport1 = Airport('1', 20, 11, 'L')
airport2 = Airport('2', 100, 100, 'L')
airport3 = Airport('3', 50, 100, 'L')
airport4 = Airport('4', 1, 2, 'L')
manager.addAirport(airport1)
manager.addAirport(airport2)
manager.addAirport(airport3)
manager.addAirport(airport4)

manager.addFlight('1', '2', 'S', 5, 1)
manager.addFlight('1', '3', 'S', 1, 1)
manager.addFlight('2', '3', 'S', 3, 1)
manager.addFlight('2', '4', 'S', 1, 1)
manager.addFlight('3', '4', 'S', 1, 1)

value, route = manager.findShortestPath('1', '2', 2)
print(route)
print(value)
print(f'{manager.flights[route[0]][route[1]][0]}', end="")
for i in range(1, len(route)):
    print(f'>>{manager.flights[route[i-1]][route[i]][1]}', end="")
print()

manager.showAllFlights()
