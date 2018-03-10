import sys
import os
import time
import csv

import java.io.FileReader as FileReader
import java.io.File as File
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random

import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import opt.DiscreteChangeOneNeighbor as DiscreteChangeOneNeighbor
import opt.EvaluationFunction as EvaluationFunction
import opt.GenericHillClimbingProblem as GenericHillClimbingProblem
import opt.HillClimbingProblem as HillClimbingProblem
import opt.NeighborFunction as NeighborFunction
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.example.FourPeaksEvaluationFunction as FourPeaksEvaluationFunction
import opt.ga.CrossoverFunction as CrossoverFunction
import opt.ga.SingleCrossOver as SingleCrossOver
import opt.ga.DiscreteChangeOneMutation as DiscreteChangeOneMutation
import opt.ga.GenericGeneticAlgorithmProblem as GenericGeneticAlgorithmProblem
import opt.ga.GeneticAlgorithmProblem as GeneticAlgorithmProblem
import opt.ga.MutationFunction as MutationFunction
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm
import opt.ga.UniformCrossOver as UniformCrossOver
import opt.prob.GenericProbabilisticOptimizationProblem as GenericProbabilisticOptimizationProblem
import opt.prob.MIMIC as MIMIC
import opt.prob.ProbabilisticOptimizationProblem as ProbabilisticOptimizationProblem
import shared.FixedIterationTrainer as FixedIterationTrainer
import opt.example.KnapsackEvaluationFunction as KnapsackEvaluationFunction
from array import array




"""
Commandline parameter(s):
    none
"""

# Random number generator */
random = Random()
# The number of items
NUM_ITEMS = 40
# The number of copies each
COPIES_EACH = 4
# The maximum weight for a single element
MAX_WEIGHT = 50
# The maximum volume for a single element
MAX_VOLUME = 50
# The volume of the knapsack 
KNAPSACK_VOLUME = MAX_VOLUME * NUM_ITEMS * COPIES_EACH * .4

TRAINING_ITERATIONS = {'RHC': 200000, 'SA': 200000, 'GA': 10000, 'MIMIC': 10000}
SA_TEMP = 100
SA_COOLRATE = .95
GA_POP = 200
GA_MATE = 150
GA_MUTATE = 25
MIMIC_GENERATE = 200
MIMIC_KEEP = 100

result_array = []
# create copies
fill = [COPIES_EACH] * NUM_ITEMS
copies = array('i', fill)

# create weights and volumes
fill = [0] * NUM_ITEMS
weights = array('d', fill)
volumes = array('d', fill)
for i in range(0, NUM_ITEMS):
    weights[i] = random.nextDouble() * MAX_WEIGHT
    volumes[i] = random.nextDouble() * MAX_VOLUME


# create range
fill = [COPIES_EACH + 1] * NUM_ITEMS
ranges = array('i', fill)

ef = KnapsackEvaluationFunction(weights, volumes, KNAPSACK_VOLUME, copies)
odd = DiscreteUniformDistribution(ranges)
nf = DiscreteChangeOneNeighbor(ranges)
mf = DiscreteChangeOneMutation(ranges)
cf = UniformCrossOver()
df = DiscreteDependencyTree(.1, ranges)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
pop = GenericProbabilisticOptimizationProblem(ef, odd, df)

rhc = RandomizedHillClimbing(hcp)
fit = FixedIterationTrainer(rhc, TRAINING_ITERATIONS['RHC'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
rhc_opt = ef.value(rhc.getOptimal())
print "RHC: " + str(rhc_opt)
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
print("============================")
result_array.append(['RHC', NUM_ITEMS, COPIES_EACH, MAX_WEIGHT, MAX_VOLUME, KNAPSACK_VOLUME, TRAINING_ITERATIONS['RHC'], '', '', '', round(rhc_opt,5), round(train_time,3), round(test_time,3)])


sa = SimulatedAnnealing(SA_TEMP, SA_COOLRATE, hcp)
fit = FixedIterationTrainer(sa, TRAINING_ITERATIONS['SA'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
sa_opt = ef.value(sa.getOptimal())
print "SA: " + str(sa_opt)
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
print("============================")
result_array.append(['SA', NUM_ITEMS, COPIES_EACH, MAX_WEIGHT, MAX_VOLUME, KNAPSACK_VOLUME, TRAINING_ITERATIONS['SA'], SA_TEMP, SA_COOLRATE, '', round(sa_opt,5), round(train_time,3), round(test_time,3)])


ga = StandardGeneticAlgorithm(GA_POP, GA_MATE, GA_MUTATE, gap)
fit = FixedIterationTrainer(ga, TRAINING_ITERATIONS['GA'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
ga_opt = ef.value(ga.getOptimal())
print "GA: " + str(ga_opt)
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
print("============================")
result_array.append(['GA', NUM_ITEMS, COPIES_EACH, MAX_WEIGHT, MAX_VOLUME, KNAPSACK_VOLUME, TRAINING_ITERATIONS['GA'], GA_POP, GA_MATE, GA_MUTATE, round(ga_opt,5), round(train_time,3), round(test_time,3)])


mimic = MIMIC(MIMIC_GENERATE, MIMIC_KEEP, pop)
fit = FixedIterationTrainer(mimic, TRAINING_ITERATIONS['MIMIC'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
mimic_opt = ef.value(mimic.getOptimal())
print "MIMIC: " + str(mimic_opt)
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
print("============================")
result_array.append(['MIMIC', NUM_ITEMS, COPIES_EACH, MAX_WEIGHT, MAX_VOLUME, KNAPSACK_VOLUME, TRAINING_ITERATIONS['MIMIC'], MIMIC_GENERATE, MIMIC_KEEP, '', round(mimic_opt,5), round(train_time,3), round(test_time,3)])



with open("data/wine/knapsack_results.csv", "a") as result_file:
    writer = csv.writer(result_file)
    writer.writerows(result_array)
