

def work(foo):
    foo.do_task()

from multiprocessing import Pool

pool = Pool()
pool.map(work)
pool.close()
pool.join()
