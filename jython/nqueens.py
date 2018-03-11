"""
For the nqueens problem from the Java file.

-Athira Nair
"""
import random
import csv
import time

import opt.ga.NQueensFitnessFunction as NQueensFitnessFunction
import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscretePermutationDistribution as DiscretePermutationDistribution
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import opt.DiscreteChangeOneNeighbor as DiscreteChangeOneNeighbor
import opt.EvaluationFunction as EvaluationFunction
import opt.GenericHillClimbingProblem as GenericHillClimbingProblem
import opt.HillClimbingProblem as HillClimbingProblem
import opt.NeighborFunction as NeighborFunction
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.SwapNeighbor as SwapNeighbor
from opt.example import *
import opt.ga.CrossoverFunction as CrossoverFunction
import opt.ga.DiscreteChangeOneMutation as DiscreteChangeOneMutation
import opt.ga.SingleCrossOver as SingleCrossOver
import opt.ga.GenericGeneticAlgorithmProblem as GenericGeneticAlgorithmProblem
import opt.ga.GeneticAlgorithmProblem as GeneticAlgorithmProblem
import opt.ga.MutationFunction as MutationFunction
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm
import opt.ga.SwapMutation as SwapMutation
import opt.prob.GenericProbabilisticOptimizationProblem as GenericProbabilisticOptimizationProblem
import opt.prob.MIMIC as MIMIC
import opt.prob.ProbabilisticOptimizationProblem as ProbabilisticOptimizationProblem
import shared.FixedIterationTrainer as FixedIterationTrainer

N = 50
TRAINING_ITERATIONS = {'RHC': 200000, 'SA': 200000, 'GA': 1000, 'MIMIC': 400}
SA_TEMP = 1E1
SA_COOLRATE = .1
GA_POP = 400
GA_MATE = 0
GA_MUTATE = 10
MIMIC_GENERATE = 4000
MIMIC_KEEP = 100
result_array=[]

ranges = [random.randint(1,N) for i in range(N)]
ef = NQueensFitnessFunction()
odd = DiscretePermutationDistribution(N)
nf = SwapNeighbor()
mf = SwapMutation()
cf = SingleCrossOver()
df = DiscreteDependencyTree(.1)
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
# print "RHC: Board Position: "
# print(ef.boardPositions())
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
result_array.append(['RHC', N, TRAINING_ITERATIONS['RHC'], '', '', '', round(rhc_opt,5), round(train_time,3), round(test_time,3)])

print("============================")

sa = SimulatedAnnealing(SA_TEMP, SA_COOLRATE, hcp)
fit = FixedIterationTrainer(sa, TRAINING_ITERATIONS['SA'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
sa_opt = ef.value(sa.getOptimal())
print "SA: " + str(sa_opt)
# print("SA: Board Position: ")
# print(ef.boardPositions())
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
result_array.append(['SA', N, TRAINING_ITERATIONS['SA'], SA_TEMP, SA_COOLRATE, '', round(sa_opt,5), round(train_time,3), round(test_time,3)])

print("============================")

ga = StandardGeneticAlgorithm(GA_POP, GA_MATE, GA_MUTATE, gap)
fit = FixedIterationTrainer(ga, TRAINING_ITERATIONS['GA'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
starttime = time.time()
ga_opt = ef.value(ga.getOptimal())
print "GA: " + str(ga_opt)
# print("GA: Board Position: ")
# print(ef.boardPositions())
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
result_array.append(['GA', N, TRAINING_ITERATIONS['GA'], GA_POP, GA_MATE, GA_MUTATE, round(ga_opt,5), round(train_time,3), round(test_time,3)])

print("============================")

mimic = MIMIC(MIMIC_GENERATE, MIMIC_KEEP, pop)
fit = FixedIterationTrainer(mimic, TRAINING_ITERATIONS['MIMIC'])
starttime = time.time()
fit.train()
train_time = (time.time() - starttime)
print "Train Time : %0.03f" % train_time
mimic_opt = ef.value(mimic.getOptimal())
print "MIMIC: " + str(mimic_opt)
# print("MIMIC: Board Position: ")
# print(ef.boardPositions())
test_time = (time.time() - starttime)
print "Test time : %0.03f" % test_time
result_array.append(['MIMIC', N, TRAINING_ITERATIONS['MIMIC'], MIMIC_GENERATE, MIMIC_KEEP, '', round(mimic_opt,5), round(train_time,3), round(test_time,3)])



with open("data/wine/nqueens_results.csv", "a") as result_file:
    writer = csv.writer(result_file)
    writer.writerows(result_array)
