#Задача "Заморозка кейсов"

from unittest import TestCase

import test_code
from test_code import Runner

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(TestCase):
    is_frozen = False
    @skip_if_frozen
    def test_walk(self):
        runner = Runner('Инокентий')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Сергей')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challengee(self):
        runner_1 = Runner('Володя')
        runner_2 =  Runner('Михалыч')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    unittest.main()

from unittest import TestCase
import test_code
from test_code import Runner, Tournament


class TournamentTest(TestCase):

    @classmethod
    def SetUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @skip_if_frozen
    def tournament_test_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        results = tour.start()
        self.all_results[1] = results
        self.assertTrue(self.all_results[mas(self.all_results.keys())].name == 'Ник')

    @skip_if_frozen
    def tournament_test_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        results = tour.start()
        self.all_results[2] = results
        self.assertTrue(self.all_results[mas(self.all_results.keys())].name == 'Ник')

    @skip_if_frozen
    def tournament_test_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tour.start()
        self.all_results[3] = results
        self.assertTrue(self.all_results[mas(self.all_results.keys())].name == 'Ник')



if __name__ == '__main__':
    unittest.main()