# pylint: disable=old-style-class
from NiaPy.tests.test_algorithm import AlgorithmTestCase, MyBenchmark
from NiaPy.algorithms.basic import FlowerPollinationAlgorithm


class FPATestCase(AlgorithmTestCase):

    def test_custom_works_fine(self):
        fpa_custom = FlowerPollinationAlgorithm(NP=10, D=self.D, nFES=self.nFES, nGEN=self.nGEN, p=0.5, benchmark=MyBenchmark(), seed=self.seed)
        fpa_customc = FlowerPollinationAlgorithm(NP=10, D=self.D, nFES=self.nFES, nGEN=self.nGEN, p=0.5, benchmark=MyBenchmark(), seed=self.seed)
        AlgorithmTestCase.algorithm_run_test(self, fpa_custom, fpa_customc)

    def test_griewank_works_fine(self):
        fpa_griewank = FlowerPollinationAlgorithm(D=self.D, NP=20, nFES=self.nFES, nGEN=self.nGEN, p=0.5, benchmark='griewank', seed=self.seed)
        fpa_griewankc = FlowerPollinationAlgorithm(D=self.D, NP=20, nFES=self.nFES, nGEN=self.nGEN, p=0.5, benchmark='griewank', seed=self.seed)
        AlgorithmTestCase.algorithm_run_test(self, fpa_griewank, fpa_griewankc)

    def test_griewank_works_fine_with_beta(self):
        fpa_beta_griewank = FlowerPollinationAlgorithm(D=self.D, NP=20, nFES=self.nFES, nGEN=self.nGEN, p=0.5, beta=1.2, benchmark='griewank', seed=self.seed)
        fpa_beta_griewankc = FlowerPollinationAlgorithm(D=self.D, NP=20, nFES=self.nFES, nGEN=self.nGEN, p=0.5, beta=1.2, benchmark='griewank', seed=self.seed)
        AlgorithmTestCase.algorithm_run_test(self, fpa_beta_griewank, fpa_beta_griewankc)
