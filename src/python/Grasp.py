from src.python.DataStructure import Coverage, Solution
from src.python.parseInstance import Parser
from copy import deepcopy
import matplotlib.pyplot as plt
from scipy.spatial import distance

import random

statistics = {i : [] for i in range(15)}

class Grasp:

    def __init__(self, data, maxDistance, MaxFacilityNumber, graspIterations):
        self.parser = Parser(data)
        self.d = maxDistance
        self.k = MaxFacilityNumber
        self.coverage = Coverage(self.parser.Nodes, maxDistance)
        self.solutions = []
        self.bestSolution = []

        sol = self.grasp_procedure(self.coverage)
        self.solutions.append({"solution" : sol, "covered_demand" : self.coverage.get_solution_demand(sol)})
        statistics[0] += [self.coverage.get_solution_demand(sol) / self.parser.totalDemand]

        counter = 0
        iter = 1
        while counter < graspIterations :
            newSol = self.grasp_procedure(self.coverage)
            self.solutions.append({"solution" : newSol, "covered_demand" : self.coverage.get_solution_demand(newSol)})

            statistics[iter] += [self.coverage.get_solution_demand(newSol) / self.parser.totalDemand]

            if self.coverage.get_solution_demand(newSol) > self.coverage.get_solution_demand(sol):
                sol = newSol
            else :
                counter += 1

            iter += 1
        self.bestSolution = {"solution" : sol, "covered_demand" : self.coverage.get_solution_demand(sol)}



    def grasp_procedure(self, coverage):

        cover = deepcopy(coverage)
        sol = []
        while len(sol) < self.k and cover.coverage_dict :
            RCL = self.construct_RCL(cover)
            s = random.choice(RCL)
            sol.append(s)
            cover.update_coverage(s)

        sol = self.localSearch(sol, coverage)

        return sol


    def construct_RCL(self, coverage):
        coverage = deepcopy(coverage.coverage_dict)
        RCL = []
        while len(RCL) < self.k and coverage :
            s = max(coverage, key= lambda i: coverage[i]["d"])
            RCL.append(s)
            del coverage[s]
        return RCL

    def localSearch(self, solution, coverage):
        sol = Solution(solution, deepcopy(coverage))

        changed = True
        while changed:
            changed = False
            n = sol.compute_neighborhood()

            for candidate in n:
                for s in sol.solution:
                    if sol.demand < coverage.get_solution_demand([node for node in sol.solution if node != s] + [candidate]):
                        sol = Solution([node for node in sol.solution if node != s] + [candidate], coverage)
                        changed = True
                        break

        return sol.solution

    def plot_solution(self):
        s = []

        for _ in self.bestSolution["solution"]:
            cov = self.coverage.get_covered_nodes(_)
            for n in cov :
                if n not in s :
                    s.append(n)


        nodesbynum = self.parser.nodesbynum
        nodesbypos = self.parser.nodesbypos
        points = self.parser.points


        for i in range(len(s)):
            s[i] = nodesbynum[s[i]]

        sol = [nodesbynum[i] for i in self.bestSolution["solution"]]

        for point in points:
            plt.plot(point[0], point[1], marker='o', color='r', ls='', markersize= 3)

        for point in s:
            plt.plot(point[0], point[1], marker='o', color='b', ls='',markersize= 3)

        for point in sol:
            plt.plot(point[0], point[1], marker='o', color='g', ls='',markersize= 6)

        for s in sol:
            for pt in s:
                if distance.euclidean(s,pt) <= self.d :
                    print(pt,s)
                    plt.plot([s[0],pt[0]], [s[1], pt[1]], color='b',linewidth=1)

        plt.show()






g = Grasp("/data1", 500, 6, 10)

print(g.solutions)
print(g.bestSolution)
print(g.coverage.get_coverage_matrix())
#g.plot_solution()
print(statistics)