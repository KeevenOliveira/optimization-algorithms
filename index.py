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


fitness = mlrose.CustomFitness(fitnessFunction)

problem = mlrose.DiscreteOpt(length=12, fitness_fn=fitness,
                             maximize=False, max_val=10)

bestSolutionHillClimb, bestCostHillClimb = mlrose.hill_climb(problem, random_state=4)

print(bestSolutionHillClimb, bestCostHillClimb)

printFlights(bestSolutionHillClimb)

print(" ------------------ ")

bestSolutionSimulated, bestCostSimulated = mlrose.simulated_annealing(problem)
print(bestSolutionSimulated, bestCostSimulated)

printFlights(bestSolutionSimulated)

print(" ------------------ ")

bestSolutionSimulatedDecay, bestCostSimulatedDecay = mlrose.simulated_annealing(problem,
                                                                                schedule=mlrose
                                                                                .decay.GeomDecay(init_temp=10000),
                                                                                random_state=1)
# bestSolutionSimulatedDecay, bestCostSimulatedDecay = mlrose.simulated_annealing(problem,
# schedule=mlrose.decay.ArithDecay())
# (schedule=mlrose.decay.ExpDecay())

print(bestSolutionSimulatedDecay, bestCostSimulatedDecay)

printFlights(bestSolutionSimulatedDecay)
