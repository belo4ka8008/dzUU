#освоить методы, которые содержит класс TestCase.
from unittest import TestCase
import test_code
from test_code import Runner, Tournament


class TournamentTest(TestCase):

    @classmethod
    def SetUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def tournament_test_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        results = tour.start()
        self.all_results[1] = results
        self.assertTrue(self.all_results[mas(self.all_results.keys())].name == 'Ник')

    def tournament_test_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        results = tour.start()
        self.all_results[2] = results
        self.assertTrue(self.all_results[mas(self.all_results.keys())].name == 'Ник')

    def tournament_test_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tour.start()
        self.all_results[3] = results
        self.assertTrue(self.all_results[mas(self.all_results.keys())].name == 'Ник')


if __name__ == "__main__":
    unittest.main()