from src.python.DataStructure import Coverage, Solution
from src.python.parseInstance import Parser
from copy import deepcopy
import random

"""
Nodes = {"Jette" : {"d" : 21, "e" : {"Evere" : 7, "Forest" : 15}},
         "Evere" : {"d": 30, "e" : {"Jette": 7, "St-Gille" : 12, "Ixelles" : 14 }},
         "St-Gille" : {"d": 11, "e" : {"Evere" : 12, "Ixelles" : 8, "Uccle" : 7, "Forest" : 11 }},
         "Forest" : {"d": 7, "e" : {"St-Gille" : 11, "Uccle": 9, "Jette": 15}},
         "Uccle" : {"d": 7, "e" : {"Forest" : 9, "Ixelles" : 5, "St-Gille" : 7}},
         "Ixelles" : {"d": 24, "e" : {"Uccle": 5, "St-Gille" : 8, "Evere" : 14}}
         }

Nodes = Parser.get_Nodes()
"""

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

        counter = 0
        while counter < graspIterations :
            newSol = self.grasp_procedure(self.coverage)
            self.solutions.append({"solution" : newSol, "covered_demand" : self.coverage.get_solution_demand(newSol)})

            if self.coverage.get_solution_demand(newSol) > self.coverage.get_solution_demand(sol):
                sol = newSol
            else :
                counter += 1

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









g = Grasp("/data1", 150, 3, 4)

print(g.solutions)
print(g.bestSolution)
print(g.coverage.get_coverage_matrix())
