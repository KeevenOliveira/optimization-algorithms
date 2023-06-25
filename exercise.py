import six
import sys

sys.modules['sklearn.externals.six'] = six
import mlrose

products = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]
spaceAvailable = 3


def printSolution(solution):
    for i in range(len(solution)):
        if solution[i] == 1:
            print('%s - %s' % (products[i][0], products[i][2]))


printSolution([0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1])


def fitnessFunction(solution):
    cost = 0
    spaceSum = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            cost += products[i][2]
            spaceSum += products[i][1]
        if spaceSum > spaceAvailable:
            cost = 1
        return cost


fitnessFunction([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1])

fitness = mlrose.CustomFitness(fitnessFunction)
problem = mlrose.DiscreteOpt(length=14, fitness_fn=fitness, maximize=True, max_val=2)

print(" ------------------ ")
print("* Hill Climb *")

bestSolutionHillClimb, bestCostHillClimb = mlrose.hill_climb(problem)
print(bestSolutionHillClimb, bestCostHillClimb)
printSolution(bestSolutionHillClimb)

print(" ------------------ ")
print("* Simulated Annealing *")

bestSolutionSimulated, bestCostSimulated = mlrose.simulated_annealing(problem)
print(bestSolutionSimulated, bestCostSimulated)
printSolution(bestSolutionSimulated)

print(" ------------------- ")
print("* Algorithms generics *")
bestSolutionGeneticAlg, bestCostGeneticAlg = mlrose.genetic_alg(problem, pop_size=500, mutation_prob=0.3)
print(bestSolutionGeneticAlg, bestCostGeneticAlg)
printSolution(bestSolutionGeneticAlg)
