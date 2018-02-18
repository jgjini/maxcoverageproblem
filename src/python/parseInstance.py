from scipy.spatial import distance
import matplotlib.pyplot as plt
import numpy as np

class Parser:
    def __init__(self, nodesFile):
        self.nodeFile = nodesFile
        self.totalDemand = 0
        self.Nodes = self.get_Nodes()

    def get_Nodes(self):
        points = []
        nodesbynum = {}
        nodesbypos = {}
        counter = 1
        with open("/Users/Jurgen/PycharmProjects/maxcoverageproblem/data/nodesfile" + self.nodeFile) as file:
            for line in file:
                p = line.split(" ")
                nodesbypos[(int(p[0]),int(p[1]))] = counter
                nodesbynum[counter] = (int(p[0]),int(p[1]))
                counter += 1
                points.append((int(p[0]),int(p[1])))

        set = [3, 5, 6, 7, 8, 9, 10, 14, 15, 16, 17, 18, 19, 24, 25, 26, 27, 28, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 72, 73, 74, 75, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 217, 218, 219, 220, 223, 224, 225, 233, 236, 238, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 267, 268, 269, 270, 271, 272, 276, 277, 278, 279, 280, 285, 286, 287, 288, 293, 294, 295, 299, 300, 301, 302, 305, 306, 307, 308, 310, 311, 314, 318]

        for i in range(len(set)):
            set[i] = nodesbynum[set[i]]

        sol = [nodesbynum[38], nodesbynum[52], nodesbynum[285], nodesbynum[143], nodesbynum[126]]

        for point in points:
            plt.plot(point[0], point[1], marker='o', color='r', ls='')
        for point in set:
            plt.plot(point[0], point[1], marker='o', color='b', ls='')

        for point in sol:
            plt.plot(point[0], point[1], marker='o', color='g', ls='')

        """
        for point in points :
            if point not in sol :
                if point not in set :
                    plt.plot(point[0], point[1],marker='o', color='r', ls='')
                else :
                    plt.plot(point[0], point[1], marker='o', color='b', ls='')
            else :
                plt.plot(point[0], point[1], marker='o', color='g', ls='')
        """
        for s in sol:
            for pt in set:
                if distance.euclidean(s,pt) <= 500 :
                    print(pt,s)
                    plt.plot([s[0],pt[0]], [s[1], pt[1]], color='b',linewidth=1)
        plt.show()

        #plt.plot([409408, 436075],(409541, 436090))
        #plt.plot([409408,409541],[436075,436090])
        #plt.plot(*zip(*points), marker='o', color='r', ls='')
        #plt.plot(*zip(*[nodesbynum[38], nodesbynum[52], nodesbynum[285], [143], nodesbynum[126]]), marker = 'o', color = 'g', ls='')
        plt.show()

        finalNodes = {}
        for p1 in points:
            finalNodes[nodesbypos[p1]] = {}
            covered_nodes = {}
            for p2 in points:
                if p1 != p2:
                    covered_nodes[nodesbypos[p2]] = distance.euclidean(p1,p2)



            finalNodes[nodesbypos[p1]]["e"] = covered_nodes


        counter = 1
        with open("/Users/Jurgen/PycharmProjects/maxcoverageproblem/data/demandfiles" + self.nodeFile) as file2:
            total = 0
            for line in file2:
                finalNodes[counter]["d"] = int(line.split()[0])
                total += int(line.split()[0])
                counter += 1

        self.totalDemand = total

        return finalNodes



