import multiprocessing
from src.python.Grasp import  Grasp


def work(filenum):
    statistics = {i: [] for i in range(30)}
    statistics["file"] = filenum
    for i in range(1, 30):
        g = Grasp("/data" + str(filenum), 150, i, 3, statistics)
        print(statistics)
    print("File " + str(filenum) + " Done   :   ")
    print(statistics)
    return


if __name__  == '__main__' :
    jobs = []
    print("hello")
    for i in range(1,5):
        p = multiprocessing.Process(target=work, args=(i,))
        jobs.append(p)
        p.start()