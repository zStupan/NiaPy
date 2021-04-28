# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

from niapy.algorithms.modified import MultiStrategyDifferentialEvolutionMTS
from niapy.algorithms.basic.de import CrossCurr2Best1, CrossBest1
from niapy.task.task import StoppingTask, OptimizationType
from niapy.benchmarks import Sphere

# we will run Differential Evolution for 5 independent runs
for i in range(5):
	task = StoppingTask(D=10, nFES=10000, optType=OptimizationType.MINIMIZATION, benchmark=Sphere())
	algo = MultiStrategyDifferentialEvolutionMTS(NP=50, F=0.5, CR=0.9, strategies=(CrossBest1, CrossCurr2Best1))
	best = algo.run(task)
	print('%s -> %s' % (best[0], best[1]))

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
