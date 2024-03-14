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
        # check airport exists or not
        if airport.id in self.airports.keys():  # exist
            return -1

        # add airport infor into DS
        self.airports[airport.id] = {'x': airport.x, 'y': airport.y, 'its_type': airport.its_type,
                                     'index': self.numberOfAirport}

        # Allocate memory to save all flights in this airport
        for i in range(0, self.numberOfAirport):
            self.flights[i].append(-1)
        self.numberOfAirport += 1
        self.flights.append([-1] * self.numberOfAirport)
        return self.numberOfAirport - 1

    def addFlight(self, src: str, dest: str, its_types, time, cost):
        # check 2 airport exists or not
        if src not in self.airports.keys() or dest not in self.airports.keys():  # not exist
            return -1

        # check plane type
        if self.types[its_types] > self.types[self.airports[src]['its_type']] or self.types[its_types] > self.types[
            self.airports[dest]['its_type']]:
            return -2

        # add flight into DS
        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        self.flights[indexSrc][indexDest] = [src, dest, time, cost, its_types]
        self.flights[indexDest][indexSrc] = [dest, src, time, cost, its_types]
        return 0

    def deleteFlight(self, src: str, dest: str):
        # Check 2 airports exist
        if src not in self.airports.keys() or dest not in self.airports.keys():
            return -1

        # Delete that flight
        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        self.flights[indexSrc][indexDest] = -1
        self.flights[indexDest][indexSrc] = -1
        return 0

    def deleteAirport(self, id):
        # Check airport exists or not
        if id not in self.airports.keys():
            return -1

        # Delete all flight in airport from DS
        temp = self.airports[id]['index']
        for i in range(0, self.numberOfAirport):
            self.flights[i].pop(temp)
        self.flights.pop(temp)

        # Delete airport infor from DS
        self.airports.pop(id)

        # Change structure of adj matrix
        for i in self.airports.keys():
            self.airports[i]['index'] -= 1
        self.numberOfAirport -= 1
        return 0

    def updateAirport(self, airport):
        if airport.id not in self.airports.keys():
            return -1
        index = self.airports[airport.id]['index']
        for i in range(0, self.numberOfAirport):
            if self.flights[index][i] == -1:
                continue
            if self.types[self.flights[index][i][4]] > self.types[airport.its_type]:
                return -2
        self.airports[airport.id] = {'x': airport.x, 'y': airport.y, 'its_type': airport.its_type,
                                     'index': self.airports[airport.id]['index']}
        return 0

    def updateFlight(self, src: str, dest: str, its_types, time, cost):
        if src not in self.airports.keys() or dest not in self.airports.keys():
            return -1

            # check plane type
        if self.types[its_types] > self.types[self.airports[src]['its_type']] or self.types[its_types] > self.types[
            self.airports[dest]['its_type']]:
            return -2

        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        print(indexSrc, indexDest)
        self.flights[indexSrc][indexDest] = [src, dest, time, cost, its_types]
        self.flights[indexDest][indexSrc] = [dest, src, time, cost, its_types]

    def findFlight(self, src: str, dest: str):
        if src not in self.airports.keys() or dest not in self.airports.keys():
            return -1
        indexSrc = self.airports[src]['index']
        indexDest = self.airports[dest]['index']
        return self.flights[indexSrc][indexDest]

    def findAirport(self, id):
        if id not in self.airports.keys():  # not exist
            return -1
        return self.airports[id]

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
