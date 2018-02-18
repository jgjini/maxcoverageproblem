from DataStructure import Coverage, Solution
from copy import deepcopy
from parseInstance import Parser
import random
Nodes = {"Jette" : {"d" : 21, "e" : {"Evere" : 7, "Forest" : 15}},
         "Evere" : {"d": 30, "e" : {"Jette": 7, "St-Gille" : 12, "Ixelles" : 14 }},
         "St-Gille" : {"d": 11, "e" : {"Evere" : 12, "Ixelles" : 8, "Uccle" : 7, "Forest" : 11 }},
         "Forest" : {"d": 7, "e" : {"St-Gille" : 11, "Uccle": 9, "Jette": 15}},
         "Uccle" : {"d": 7, "e" : {"Forest" : 9, "Ixelles" : 5, "St-Gille" : 7}},
         "Ixelles" : {"d": 24, "e" : {"Uccle": 5, "St-Gille" : 8, "Evere" : 14}}
         }

Nodes = Parser.get_Nodes()
class Grasp:
    def __init__(self, Nodes, d, k):
        self.d = d
        self.k = k
        self.coverage = Coverage(Nodes,d)
        print(self.coverage.coverage_dict)
        n = [38, 52, 285, 143, 126]
        s = set()
        for _ in n :
            cov = self.coverage.get_covered_nodes(_)
            for c in cov :
                s.add(c)
        print(s)
        sol = self.grasp_procedure(self.coverage)
        print(sol)
        print(self.coverage.get_solution_demand(sol))
        changed = True
        counter = 0
        while counter < 3 :
            changed = False
            newSol = self.grasp_procedure(self.coverage)
            print(newSol)
            print(self.coverage.get_solution_demand(newSol))
            if self.coverage.get_solution_demand(newSol) > self.coverage.get_solution_demand(sol):
                sol = newSol
                changed = True
            else :
                counter += 1


        print(sol)
        print("Covered Demand : ", self.coverage.get_solution_demand(sol))



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
        print(solution)
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









g = Grasp(Nodes, 500, 5)

