# traveling salesman algorithm implementation in jython
# This also prints the index of the points of the shortest route.
# To make a plot of the route, write the points at these indexes 
# to a file and plot them in your favorite tool.
import sys
import os
import time

import java.io.FileReader as FileReader
import java.io.File as File
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random

import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import dist.DiscretePermutationDistribution as DiscretePermutationDistribution
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
import opt.example.TravelingSalesmanEvaluationFunction as TravelingSalesmanEvaluationFunction
import opt.example.TravelingSalesmanRouteEvaluationFunction as TravelingSalesmanRouteEvaluationFunction
import opt.SwapNeighbor as SwapNeighbor
import opt.ga.SwapMutation as SwapMutation
import opt.example.TravelingSalesmanCrossOver as TravelingSalesmanCrossOver
import opt.example.TravelingSalesmanSortEvaluationFunction as TravelingSalesmanSortEvaluationFunction
import shared.Instance as Instance
import util.ABAGAILArrays as ABAGAILArrays

from array import array

import csv


"""
Commandline parameter(s):
    none
"""

# set N value.  This is the number of points
N = 100
TRAINING_ITERATIONS = {'RHC': 200000, 'SA': 200000, 'GA': 1000, 'MIMIC': 200}
SA_TEMP = 1E12
SA_COOLRATE = .999
GA_POP = 2000
GA_MATE = 1500
GA_MUTATE = 250
MIMIC_GENERATE = 600
MIMIC_KEEP = 10
result_array = []

random = Random()

points = [[0 for x in xrange(2)] for x in xrange(N)]
for i in range(0, len(points)):
    points[i][0] = random.nextDouble()
    points[i][1] = random.nextDouble()

ef = TravelingSalesmanRouteEvaluationFunction(points)
odd = DiscretePermutationDistribution(N)
nf = SwapNeighbor()
mf = SwapMutation()
cf = TravelingSalesmanCrossOver(ef)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)

rhc = RandomizedHillClimbing(hcp)
fit = FixedIterationTrainer(rhc, TRAINING_ITERATIONS['RHC'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
rhc_opt = ef.value(rhc.getOptimal())
print "RHC Inverse of Distance: " + str(rhc_opt)
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
print "Route:"
path = []
for x in range(0,N):
    path.append(rhc.getOptimal().getDiscrete(x))
print path
print("============================")
result_array.append(['RHC', N, TRAINING_ITERATIONS['RHC'], '', '', '', round(rhc_opt,5), round(train_time,3), round(test_time,3)])


sa = SimulatedAnnealing(SA_TEMP, SA_COOLRATE, hcp)
fit = FixedIterationTrainer(sa, TRAINING_ITERATIONS['SA'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
sa_opt = ef.value(sa.getOptimal())
print "SA Inverse of Distance: " + str(sa_opt)
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
print "Route:"
path = []
for x in range(0,N):
    path.append(sa.getOptimal().getDiscrete(x))
print path
print("============================")
result_array.append(['SA', N, TRAINING_ITERATIONS['SA'], SA_TEMP, SA_COOLRATE, '', round(sa_opt,5), round(train_time,3), round(test_time,3)])


ga = StandardGeneticAlgorithm(GA_POP, GA_MATE, GA_MUTATE, gap)
fit = FixedIterationTrainer(ga, TRAINING_ITERATIONS['GA'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
ga_opt = ef.value(ga.getOptimal())
print "GA Inverse of Distance: " + str(ga_opt)
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
print "Route:"
path = []
for x in range(0,N):
    path.append(ga.getOptimal().getDiscrete(x))
print path
print("============================")
result_array.append(['GA', N, TRAINING_ITERATIONS['GA'], GA_POP, GA_MATE, GA_MUTATE, round(ga_opt,5), round(train_time,3), round(test_time,3)])


# for mimic we use a sort encoding
ef = TravelingSalesmanSortEvaluationFunction(points);
fill = [N] * N
ranges = array('i', fill)
odd = DiscreteUniformDistribution(ranges);
df = DiscreteDependencyTree(.1, ranges);
pop = GenericProbabilisticOptimizationProblem(ef, odd, df);

mimic = MIMIC(MIMIC_GENERATE, MIMIC_KEEP, pop)
fit = FixedIterationTrainer(mimic, TRAINING_ITERATIONS['MIMIC'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
mimic_opt = ef.value(mimic.getOptimal())
print "MIMIC Inverse of Distance: " + str(mimic_opt)
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
print "Route:"
path = []
optimal = mimic.getOptimal()
fill = [0] * optimal.size()
ddata = array('d', fill)
for i in range(0,len(ddata)):
    ddata[i] = optimal.getContinuous(i)
order = ABAGAILArrays.indices(optimal.size())
ABAGAILArrays.quicksort(ddata, order)
print order
print("============================")
result_array.append(['MIMIC', N, TRAINING_ITERATIONS['MIMIC'], MIMIC_GENERATE, MIMIC_KEEP, '', round(mimic_opt,5), round(train_time,3), round(test_time,3)])


with open("data/wine/tsp_results.csv", "a") as result_file:
    writer = csv.writer(result_file)
    writer.writerows(result_array)
