# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

import random
from niapy.algorithms.basic import DynNpDifferentialEvolution
from niapy.task import StoppingTask
from niapy.benchmarks import Sphere

#we will run Differential Evolution for 5 independent runs
for i in range(5):
	task = StoppingTask(D=10, nFES=10000, benchmark=Sphere())
	algo = DynNpDifferentialEvolution(NP=120, F=0.5, CR=0.9, pmax=25)
	best = algo.run(task=task)
	print('%s -> %s' % (best[0], best[1]))

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
