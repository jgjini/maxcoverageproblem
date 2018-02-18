from copy import deepcopy

class Coverage :
    def __init__(self, nodes, coverageDistance):
        self.nodes = deepcopy(nodes)
        self.d = coverageDistance
        self.coverage_dict = self.construct_coverage_matrix(self.nodes)

    def get_covered_nodes(self, current):
        coverage = [node for node in self.nodes[current]["e"] if self.nodes[current]["e"][node] <= self.d]
        coverage.append(current)
        return coverage

    def get_coverage_matrix(self):
        matrix =  [[0 for elem in self.nodes] for elem in self.nodes]
        demand = [0 for elem in self.nodes]

        for elem in self.coverage_dict:
            demand[elem-1] = self.nodes[elem]["d"]
            for n in self.coverage_dict[elem]["c"]:
                matrix[elem-1][n-1] = 1
        print(demand)
        return matrix

    def get_covered_demand(self, nodes):
        return sum([self.nodes[node]["d"] for node in nodes])

    def get_solution_demand(self, solution):
        covered_nodes = [self.get_covered_nodes(curr) for curr in solution]
        covered_set = set()
        for cov in covered_nodes:
            for node in cov :
                covered_set.add(node)
        return self.get_covered_demand(covered_set)

    def construct_coverage_matrix(self, Nodes):
        return {node: {"d": self.get_covered_demand(self.get_covered_nodes(node)), "c": self.get_covered_nodes(node)} for node in Nodes}

    def update_coverage(self, chosen_node):
        covered_nodes = self.get_covered_nodes(chosen_node)

        for node in covered_nodes:
            del self.nodes[node]
            
        for node in self.nodes :
            for covered_node in covered_nodes:
                try :
                    del self.nodes[node]['e'][covered_node]
                except :
                    continue
        self.coverage_dict = self.construct_coverage_matrix(self.nodes)



class Solution:
    def __init__(self, sol, covering):
        self.solution = sol
        self.covering = covering
        self.demand = covering.get_solution_demand(self.solution)

    def compute_neighborhood(self):
        covered_nodes = [self.covering.get_covered_nodes(curr) for curr in self.solution]
        covered_set = set()
        for cov in covered_nodes:
            for node in cov :
                if node not in self.solution:
                    covered_set.add(node)

        return covered_set

