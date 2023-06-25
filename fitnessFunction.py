import six
import sys

sys.modules['sklearn.externals.six'] = six
import mlrose

people = [('Lisboa', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Bruxelas', 'BRU'),
          ('Londres', 'LHR')]
destination = 'FCO'
flights = {}

for line in open('mock/flights.txt'):
    origin, destination, departure, arrival, price = line.split(',')
    flights.setdefault((origin, destination), [])
    flights[(origin, destination)].append((departure, arrival, int(price)))


def fitnessFunction(schedule):
    flightId = -1
    totalPrice = 0
    for i in range(len(schedule) // 2):
        origin = people[i][1]
        flightId += 1
        outbound = flights[(origin, destination)][schedule[flightId]]
        totalPrice += outbound[2]
        flightId += 1
        turn = flights[(destination, origin)][schedule[flightId]]
        totalPrice += turn[2]

    return totalPrice


fitness = mlrose.CustomFitness(fitnessFunction)

problem = mlrose.DiscreteOpt(length=12, fitness_fn=fitness,
                             maximize=False, max_val=10)
