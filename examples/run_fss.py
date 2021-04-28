# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

import random
from niapy.algorithms.basic import FishSchoolSearch
from niapy.task import StoppingTask
from niapy.benchmarks import Sphere

#we will run Fish School Search for 5 independent runs
for i in range(5):
    task = StoppingTask(D=10, nFES=10000, benchmark=Sphere())
    algo = FishSchoolSearch(NP=20)
    best = algo.run(task)
    print('%s -> %f' % (best[0], best[1]))

