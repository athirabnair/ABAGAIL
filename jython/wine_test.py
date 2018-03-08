"""
Implementation of randomized hill climbing, simulated annealing, and genetic algorithm to
find optimal weights to a neural network that is classifying wine as either good or bad quality

Based on AbaloneTest.java

-Athira Nair
"""

from __future__ import with_statement

import os
import csv
import time
from operator import itemgetter
import random

from func.nn.backprop import BackPropagationNetworkFactory
from shared import SumOfSquaresError, DataSet, Instance
from opt.example import NeuralNetworkOptimizationProblem

import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm


INPUT_FILE = os.path.join("..", "..", "..", "Data", "winequality-white-modified.csv")

INPUT_LAYER = 11
HIDDEN_LAYER = 9
OUTPUT_LAYER = 1
#TRAINING_ITERATIONS = 100
TRAINING_ITERATIONS = {'RHC':2000, 'SA': 2000, 'GA':1000}

"""
Defaults:

HIDDEN_LAYER = 9
    oa.append(RandomizedHillClimbing(nnop[0]))
    oa.append(SimulatedAnnealing(1E11, .95, nnop[1]))
    oa.append(StandardGeneticAlgorithm(200, 100, 10, nnop[2]))

"""

def initialize_instances():
    """Read the winequality-white.csv CSV data into a list of instances."""
    instances = []

    # Read in the abalone.txt CSV file
    with open(INPUT_FILE, "r") as wine:
        reader = csv.reader(wine)

        for row in reader:
            instance = Instance([float(value) for value in row[:-1]])
            instance.setLabel(Instance(0 if float(row[-1]) < 0.5 else 1))
            instances.append(instance)

    return instances


def train(oa, network, oaName, instances, measure):
    """Train a given network on a set of instances.

    :param OptimizationAlgorithm oa:
    :param BackPropagationNetwork network:
    :param str oaName:
    :param list[Instance] instances:
    :param AbstractErrorMeasure measure:
    """
    print "\nError results for %s\n---------------------------" % (oaName,)
    error_array = []
    for iteration in xrange(TRAINING_ITERATIONS[oaName]):
        oa.train()

        error = 0.00
        for instance in instances:
            network.setInputValues(instance.getData())
            network.run()

            output = instance.getLabel()
            output_values = network.getOutputValues()
            example = Instance(output_values, Instance(output_values.get(0)))
            error += measure.value(output, example)

        print "%d %0.03f" % (iteration,error)
        error_array.append([iteration+1, round(error,3)])

    filename = 'data/wine/error_' + oaName + '_' + str(TRAINING_ITERATIONS[oaName]) + '.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(error_array)
    print 'wrote to file {}'.format(filename)


def main():
    """Run algorithms on the wine dataset."""
    instances = initialize_instances()
    training_indices = random.sample(xrange(len(instances)), int(0.8 * len(instances)))
    training_instances = itemgetter(*training_indices)(instances)
    test_indices = list(set(range(len(instances))) - set(training_indices))
    test_instances = itemgetter(*test_indices)(instances)
    factory = BackPropagationNetworkFactory()
    measure = SumOfSquaresError()
    data_set = DataSet(training_instances)

    networks = []  # BackPropagationNetwork
    nnop = []  # NeuralNetworkOptimizationProblem
    oa = []  # OptimizationAlgorithm
    oa_names = ["RHC", "SA", "GA"]
    results = ""
    # result_array = [["Algorithm", "# Correctly Classified", "# Incorrectly Classified", "Training Time", "Testing Time", "Number of Iterations"]]
    result_array = []

    for name in oa_names:
        classification_network = factory.createClassificationNetwork([INPUT_LAYER, HIDDEN_LAYER, OUTPUT_LAYER])
        networks.append(classification_network)
        nnop.append(NeuralNetworkOptimizationProblem(data_set, classification_network, measure))

    oa.append(RandomizedHillClimbing(nnop[0]))
    oa.append(SimulatedAnnealing(1E11, .95, nnop[1]))
    oa.append(StandardGeneticAlgorithm(200, 100, 10, nnop[2]))

    for i, name in enumerate(oa_names):
        start = time.time()
        correct = 0
        incorrect = 0

        train(oa[i], networks[i], oa_names[i], training_instances, measure)
        end = time.time()
        training_time = end - start

        optimal_instance = oa[i].getOptimal()
        networks[i].setWeights(optimal_instance.getData())

        start = time.time()
        for instance in test_instances:
            networks[i].setInputValues(instance.getData())
            networks[i].run()

            predicted = instance.getLabel().getContinuous()
            actual = networks[i].getOutputValues().get(0)

            if abs(predicted - actual) < 0.5:
                correct += 1
            else:
                incorrect += 1

        end = time.time()
        testing_time = end - start

        results += "\nResults for %s: \nCorrectly classified %d instances." % (name, correct)
        results += "\nIncorrectly classified %d instances.\nPercent correctly classified: %0.03f%%" % (incorrect, float(correct)/(correct+incorrect)*100.0)
        results += "\nTraining time: %0.03f seconds" % (training_time,)
        results += "\nTesting time: %0.03f seconds" % (testing_time,)
        results += "\nNumber of iterations: %d\n" % (TRAINING_ITERATIONS[oa_names[i]])
        result_array.append([name, correct, incorrect, float(correct)/(correct+incorrect)*100.0, round(training_time,3), round(testing_time,3), TRAINING_ITERATIONS[oa_names[i]]])
    print results


    with open("data/wine/test_results.csv","a") as result_file:
        writer = csv.writer(result_file)
        writer.writerows(result_array)

if __name__ == "__main__":
    main()

