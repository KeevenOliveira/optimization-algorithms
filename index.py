from fitnessFunction import fitnessFunction

people = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

flights = {}
destination = 'FCO'

for line in open('mock/flights.txt'):
    print(line)
    origin, destination, departure, arrival, price = line.split(',')
    flights.setdefault((origin, destination), [])
    flights[(origin, destination)].append((departure, arrival, int(price)))


schedule = [1, 2, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]


def printFlights(schedule):
    flightId = -1
    totalPrice = 0
    for i in range(len(schedule) // 2):
        cityName = people[i][0]
        origin = people[i][1]
        flightId += 1
        outbound = flights[(origin, destination)][schedule[flightId]]
        totalPrice += outbound[2]
        flightId += 1
        turn = flights[(destination, origin)][schedule[flightId]]
        totalPrice += turn[2]
        print('%10s%10s %5s-%5s %3s %5s-5%s %3s' % (cityName, origin, outbound[0], outbound[1],
                                                    outbound[2], turn[0], turn[1], turn[2]))
    print('Total price: ', totalPrice)


print(fitnessFunction(schedule))
