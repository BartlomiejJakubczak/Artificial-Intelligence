import numpy as np
import random
import matplotlib.pyplot as plt
import statistics

import time

from List1.Function import Function
from List1.PointUtils import PointUtils
from functools import reduce


# links
# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
# https://cstheory.stackexchange.com/questions/14758/tournament-selection-in-genetic-algorithms

# previous version, in order to make it work adjust other functions
def evaluationFunction(points_array, individual):
    evaluation_points = 0
    for point in points_array:
        fun_value = individual.calculateValue(point.getX())
        if point.value == 1:
            if fun_value < point.getY():
                evaluation_points += 1
        else:
            if fun_value > point.getY():
                evaluation_points += 1
    return evaluation_points


# Idea taken from Szymon Bartkowiak, implementation done by myself.
def evaluationFunction2(points_array, individual):
    evaluation_points = 0
    for point in points_array:
        fun_value = individual.calculateValue(point.getX())
        if point.value == 1:
            if fun_value > point.getY():
                wrong_fitness = calculateDistance(point, individual)
                evaluation_points -= wrong_fitness
        else:
            if fun_value < point.getY():
                wrong_fitness = calculateDistance(point, individual)
                evaluation_points -= wrong_fitness
    return evaluation_points


def calculateDistance(point, individual):
    shortest = 10000
    for x in x_range:
        distance = np.sqrt((x - point.getX()) ** 2 + (individual.calculateValue(point.getX()) - point.getY()) ** 2)
        if distance < shortest:
            shortest = distance
    return shortest


def generatePopulation(amount, left_border, right_border):
    population = []
    for i in range(amount):
        population.append(Function(left_border, right_border))
    return np.array(population)


def crossover(father, mother):  # Single-point crossover
    child1 = Function(-1, 1)
    child2 = Function(-1, 1)
    crossover_point = random.randint(1, 6)
    for current in range(1, 7):  # exclusive
        if current <= crossover_point:
            child1.setGene(current, father.getGene(current))
            child2.setGene(current, mother.getGene(current))
        else:
            child1.setGene(current, mother.getGene(current))
            child2.setGene(current, father.getGene(current))
    return child1, child2


def mutate(individual):
    for gene in range(1, 7):
        if random.random() < probability_of_mutating:
            vary = random.uniform(-5, 5) + individual.getGene(gene)  # random resetting
            individual.setGene(gene, vary)


def tournament(number_of_fighters, population):  # binary tournament -> number of fighters == 2
    best = None
    for fighter_no in range(number_of_fighters):
        ind = random.choice(population)
        if best is None or ind.getEvaluationScore() > best.getEvaluationScore():
            best = ind
    return best


def findBestInd(population):  # zamienilem dla evaluation2
    best = Function(-1, 1)
    best.setEvaluationScore(-100000000000)
    for ind in population:
        if ind.getEvaluationScore() > best.getEvaluationScore():
            best = ind
    return best


def findWorstInd(population):  # zamienilem dla evaluation2
    worst = Function(-1, 1)
    worst.setEvaluationScore(0)
    for ind in population:
        if ind.getEvaluationScore() < worst.getEvaluationScore():
            worst = ind
    return worst


def calculateAverage(population):
    evaluation_points = 0
    for individual in population:
        evaluation_points += individual.getEvaluationScore()
    return evaluation_points / len(population)


def writeEvaluationScores(array, population):
    for individual in population:
        array.append(individual.getEvaluationScore())


def graph(individual):
    axes = plt.gca()
    axes.set_xlim(min_x, max_x)
    axes.set_ylim(min_y, max_y)
    plt.scatter(
        *zip(pointUtils.coordinatesOfPoints(points_positive)))
    plt.scatter(
        *zip(pointUtils.coordinatesOfPoints(points_negative)))
    plt.plot(x_range, individual.calculateFunction(x_range))
    plt.show()


def graphMultiple(individuals):
    axes = plt.gca()
    axes.set_xlim(min_x, max_x)
    axes.set_ylim(min_y, max_y)
    plt.scatter(
        *zip(pointUtils.coordinatesOfPoints(points_positive)))
    plt.scatter(
        *zip(pointUtils.coordinatesOfPoints(points_negative)))
    for individual in individuals:
        plt.plot(x_range, individual.calculateFunction(x_range))
    plt.show()


if __name__ == "__main__":
    number_of_negative_points, number_of_positive_points, number_of_generations, number_of_functions = 50, 50, 150, 30
    probability_of_crossing, probability_of_mutating = 0.7, 0.1
    fun_range_start, fun_range_end = -10, 10

    population_list = []
    population_average = []
    best_fitnesses = []
    worst_fitnesses = []
    std_deviations = []
    best_individuals = []
    worst_individuals = []

    pointUtils = PointUtils()  # My toolbox for points

    points_positive = pointUtils.generatePoints(number_of_positive_points, (1.5, 1.5), 1, 1)
    points_negative = pointUtils.generatePoints(number_of_negative_points, (0, 0), 1, -1)
    points = np.concatenate((points_positive, points_negative), axis=0)
    points_x, points_y = pointUtils.coordinatesOfPoints(points)
    max_x = max(points_x)
    max_y = max(points_y)
    min_x = min(points_x)
    min_y = min(points_y)
    x_range = np.linspace(min_x, max_x, 100)

    # initialize first generation
    initial_population = generatePopulation(number_of_functions, fun_range_start, fun_range_end)

    # evaluate first generation
    for i in range(number_of_functions):
        initial_population[i].setEvaluationScore(evaluationFunction2(points, initial_population[i]))
        print(initial_population[i].getEvaluationScore())

    population_list.append(initial_population)
    population = initial_population

    # the algorithm
    for current_generation in range(1, number_of_generations + 1):
        print("\n===== Generation", current_generation)
        new_population = []
        while len(new_population) < number_of_functions:
            parent1 = tournament(2, population)
            parent2 = tournament(2, population)
            if random.random() < probability_of_crossing:
                child1, child2 = crossover(parent1, parent2)
                new_population.extend([child1, child2])
            else:
                new_population.extend([parent1, parent2])
        for individual in new_population:
            if random.random() < probability_of_mutating:
                mutate(individual)
                individual.setEvaluationScore(evaluationFunction2(points, individual))
            else:
                individual.setEvaluationScore(evaluationFunction2(points, individual))
        print('Evaluated', len(new_population), 'individuals')
        population = new_population  # generation replacement
        population_list.append(population)

        current_fitnesses = []
        writeEvaluationScores(current_fitnesses, population)
        std_deviations.append(statistics.stdev(current_fitnesses))

        best_individual = findBestInd(population)
        worst_individual = findWorstInd(population)
        average_individual = calculateAverage(population)

        population_average.append(average_individual)
        best_individuals.append(best_individual)
        worst_individuals.append(worst_individual)

        best_fitnesses.append(best_individual.getEvaluationScore())
        worst_fitnesses.append(worst_individual.getEvaluationScore())
        print('Min =', worst_individual.getEvaluationScore(),
              ', Max =', best_individual.getEvaluationScore(),
              ', Average =', average_individual)

    print("\n==== End of evolution")
    print('\nBest individual:', max(best_fitnesses))
    print('Worst individual:', min(worst_fitnesses))
    best_individual = reduce((lambda x, y: x if x.getEvaluationScore() > y.getEvaluationScore() else y),
                             best_individuals)
    worst_individual = reduce((lambda x, y: x if x.getEvaluationScore() < y.getEvaluationScore() else y),
                              worst_individuals)
    print("Coefficients: "
          "first ", best_individual.getA(), "second ", best_individual.getB(),
          "third ", best_individual.getC(), "fourth ", best_individual.getD(),
          "fifth ", best_individual.getE(), "sixth ", best_individual.getF())

    plt.figure("Standard deviation per generation")
    plt.plot(std_deviations)
    plt.figure("Best fitness per generation")
    plt.plot(best_fitnesses)
    plt.figure("Average fitness per generation")
    plt.plot(population_average)
    plt.figure("Best individual")
    graph(best_individual)
    plt.figure("Best individuals per generation")
    graphMultiple(best_individuals)
    plt.figure("Worst individual")
    graph(worst_individual)

    # Random search
    best_random = Function(-1, 1)
    best_random.setEvaluationScore(-10000)
    start = time.time()
    number_of_evaluations = 0
    while best_random.getEvaluationScore() != 0:
        number_of_evaluations += 1
        random = Function(fun_range_start, fun_range_end)
        random.setEvaluationScore(evaluationFunction2(points, random))
        if random.getEvaluationScore() > best_random.getEvaluationScore():
            best_random = random
    end = time.time()
    plt.figure("Random search")
    graph(best_random)
    print("Time needed to find best solution: ", end - start, " number of evaluations: ", number_of_evaluations)
