"""
For the nqueens problem from the Java file.

-Athira Nair
"""
import random

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

class NQueensTest:

    def __init__(self, n = 10):
        self.N = n

    def main(self):
        ranges = [random.randint(1,self.N) for i in range(self.N)]
        ef = NQueensFitnessFunction()
        odd = DiscretePermutationDistribution(self.N)
        nf = SwapNeighbor()
        mf = SwapMutation()
        cf = SingleCrossOver()
        df = DiscreteDependencyTree(.1)
        hcp = GenericHillClimbingProblem(ef, odd, nf)
        gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
        pop = GenericProbabilisticOptimizationProblem(ef, odd, df)

        rhc = RandomizedHillClimbing(hcp)
        fit = FixedIterationTrainer(rhc, 100)
        fit.train()
        starttime = time.time()
        print "RHC: %f" % ef.value(rhc.getOptimal())
        print "RHC: Board Position: "
        # print(ef.boardPositions())
        print "Time : %0.03f" % (time.time() - starttime)

        print("============================")

        sa = SimulatedAnnealing(1E1, .1, hcp)
        fit = FixedIterationTrainer(sa, 100)
        fit.train()

        starttime = time.time()
        print "SA: %f" % ef.value(sa.getOptimal())
        print("SA: Board Position: ")
        # print(ef.boardPositions())
        print "Time : %0.03f" % (time.time() - starttime)

        print("============================")

        starttime = time.time()
        ga = StandardGeneticAlgorithm(200, 0, 10, gap)
        fit = FixedIterationTrainer(ga, 100)
        fit.train()
        print "GA: %f" % ef.value(ga.getOptimal())
        print("GA: Board Position: ")
        # print(ef.boardPositions())
        print "Time : %0.03f" % (time.time() - starttime)

        print("============================")

        starttime = time.time()
        mimic = MIMIC(200, 10, pop)
        fit = FixedIterationTrainer(mimic, 5)
        fit.train()
        print "MIMIC: %f" % ef.value(mimic.getOptimal())
        print("MIMIC: Board Position: ")
        # print(ef.boardPositions())
        print "Time : %0.03f" % (time.time() - starttime)


if __name__ == "__main__":
    nqueens = NQueensTest(8)
    nqueens.main()