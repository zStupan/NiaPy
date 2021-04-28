# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

import random
from niapy.algorithms.modified import HybridBatAlgorithm
from niapy.task import StoppingTask
from niapy.benchmarks import Sphere

#we will run Hybrid Bat Algorithm for 5 independent runs
for i in range(5):
    task = StoppingTask(D=10, nFES=10000, benchmark=Sphere())
    algo = HybridBatAlgorithm(NP=40, A=0.5, r=0.5, F=0.5, CR=0.9, Qmin=0.0, Qmax=2.0)
    best = algo.run(task)
    print(best)
