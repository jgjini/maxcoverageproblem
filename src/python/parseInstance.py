from scipy.spatial import distance
import matplotlib.pyplot as plt
import numpy as np

class Parser:
    def __init__(self, nodesFile):
        self.nodeFile = nodesFile
        self.totalDemand = 0
        self.nodesbynum = {}
        self.nodesbypos = {}
        self.points = []

        self.Nodes = self.get_Nodes()


    def get_Nodes(self):
        counter = 1
        with open("/Users/Jurgen/PycharmProjects/maxcoverageproblem/data/nodesfile" + self.nodeFile) as file:
            for line in file:
                p = line.split(" ")
                self.nodesbypos[(int(p[0]),int(p[1]))] = counter
                self.nodesbynum[counter] = (int(p[0]),int(p[1]))
                counter += 1
                self.points.append((int(p[0]),int(p[1])))


        finalNodes = {}
        for p1 in self.points:
            finalNodes[self.nodesbypos[p1]] = {}
            covered_nodes = {}
            for p2 in self.points:
                if p1 != p2:
                    covered_nodes[self.nodesbypos[p2]] = distance.euclidean(p1,p2)



            finalNodes[self.nodesbypos[p1]]["e"] = covered_nodes


        counter = 1
        with open("/Users/Jurgen/PycharmProjects/maxcoverageproblem/data/demandfiles" + self.nodeFile) as file2:
            total = 0
            for line in file2:
                finalNodes[counter]["d"] = int(line.split()[0])
                total += int(line.split()[0])
                counter += 1

        self.totalDemand = total

        return finalNodes



