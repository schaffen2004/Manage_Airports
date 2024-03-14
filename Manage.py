from Airports import Airport, AirportManager


class Menu:
    def __init__(self):
        self.selection = 0

    @staticmethod
    def displayMenu():
        print("--------------------MENU--------------------")
        print("1. Add Airport")
        print("2. Add Flight")
        print("3. Update Airport information")
        print("4. Update Flight information")
        print("5. Delete Airport")
        print("6. Delete Flight")
        print("7. Find Airport Information")
        print("8. Find Flight Information")
        print("9. Display All Airports Information")
        print("10. Display All Flights Information")
        print("11. Find the Shortest Flight")
        print("12. Exit")
        print("--------------------------------------------")

    def selectOption(self):
        try:
            self.selection = int(input("Enter your choice: "))
            return 0
        except ValueError:
            print("Invalid Input!Please try again.")
            return -1


if __name__ == "__main__":
    menu = Menu()
    manager = AirportManager()
    while True:
        menu.displayMenu()
        inp = menu.selectOption()
        if inp == -1:
            continue
        if menu.selection == 1:
            id = input("Enter Airport ID: ")
            print("Enter airport location:")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            print('Airport types:')
            print("Small --> S")
            print("Medium --> M")
            print("Large --> L")
            its_type = input("Enter airport type: ")
            if its_type not in manager.types:
                print("Invalid airport type!")
                continue
            airport = Airport(id, x, y, its_type)
            if manager.addAirport(airport) == -1:
                print(">> Airport is already in system!")
                continue
            print(">> Airport is added to system!")
        elif menu.selection == 2:
            src = input("Enter airport source: ")
            dest = input("Enter airport destination: ")
            print('Airplane types:')
            print("Small --> S")
            print("Medium --> M")
            print("Large --> L")
            its_type = input("Enter airplane type: ")
            if its_type not in manager.types:
                print("Invalid airport type!")
                continue
            time = int(input("Enter departure time: "))
            cost = int(input("Enter departure cost: "))
            temp = manager.addFlight(src, dest, its_type, time, cost)
            if temp == -1:
                print(">> Airport in flight is not available!")
                continue
            elif temp == -2:
                print(">> Invalid plane type!")
                continue
            print(">> Flight is added to system!")
        elif menu.selection == 3:
            id = input("Enter Airport ID: ")
            print("Enter airport location:")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            print('Airport types:')
            print("Small --> S")
            print("Medium --> M")
            print("Large --> L")
            its_type = input("Enter airport type: ")
            if its_type not in manager.types:
                print("Invalid airport type!")
                continue
            airport = Airport(id, x, y, its_type)
            temp = manager.updateAirport(id)
            if temp == -1:
                print(">> Airport is not already in system!")
                continue
            if temp == -2:
                print(">> Invalid airport type!")
                continue
            print(">> Airport is updated to system!")
        elif menu.selection == 4:
            src = input("Enter airport source: ")
            dest = input("Enter airport destination: ")
            print('Airplane types:')
            print("Small --> S")
            print("Medium --> M")
            print("Large --> L")
            its_type = input("Enter airplane type: ")
            if its_type not in manager.types:
                print("Invalid airport type!")
                continue
            time = int(input("Enter departure time: "))
            cost = int(input("Enter departure cost: "))
            temp = manager.updateFlight(src, dest, its_type, time, cost)
            if temp == -1:
                print(">> Airport in flight is not available!")
                continue
            elif temp == -2:
                print(">> Invalid plane type!")
                continue
            print(">> Flight is updated to system!")
        elif menu.selection == 5:
            id = int(input("Enter airport ID: "))
            if manager.updateAirport(id) == -1:
                print(">> Airport is not already in system!")
                continue
            print(">> Airport is deleted from system!")
        elif menu.selection == 6:
            src = input("Enter airport source: ")
            dest = input("Enter airport destination: ")
            if manager.deleteFlight(src, dest) == -1:
                print(">> Airport in flight is not available!")
                continue
            print(">> Flight is deleted from system!")
        elif menu.selection == 8:
            src = input("Enter airport source: ")
            dest = input("Enter airport destination: ")
            info = manager.findFlight(src, dest)
            if info == -1:
                print(">> Flight is not available!")
                continue
            print(f"From: {info[0]}, To: {info[1]}, Time: {info[2]}, Cost: {info[3]}, Type: {info[4]}")
        elif menu.selection == 7:
            id = input("Enter id airport: ")
            info = manager.findAirport(id)
            if info == -1:
                print(">> Airport is not available!")
                continue
            print(
                f'ID: {id}, Location: {info[0], info[1]}, Type: {info[2]}, Time: {info[3]}')
        elif menu.selection == 9:
            manager.showAllAirports()
        elif menu.selection == 10:
            manager.showAllFlights()
        elif menu.selection == 11:
            src = input("Enter airport source: ")
            dest = input("Enter airport destination: ")
            while True:
                print("The shortest flight follow: ")
                print("1.Time")
                print("2.Cost")
                mode = int(input("Enter the choice number:"))
                if src == dest:
                    print(">> The destination resembles the starting point.")
                    break
                if mode == 1 or mode == 2:
                    value, route = manager.findShortestPath(src, dest, mode+1)
                    if len(route) < 2:
                        print(f"Don't have any path from {src} to {dest}")
                        break
                    print("The shortest flight follow time departure: ", value)
                    print("The flight details: ", end="")
                    print(f'{manager.flights[route[0]][route[1]][0]}', end="")
                    for i in range(1, len(route)):
                        print(f'>>{manager.flights[route[i - 1]][route[i]][1]}', end="")
                    print()
                    break
                else:
                    print(">> Invalid choice!Please enter again!")
        elif menu.selection == 12:
            exit()
        else:
            print(">> Invalid selection!Please try again!")
