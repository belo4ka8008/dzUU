#приобрести навык создания простейших Юнит-тестов
from unittest import TestCase

import test_code
from test_code import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Инокентий')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Сергей')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challengee(self):
        runner_1 = Runner('Володя')
        runner_2 =  Runner('Михалыч')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    unittest.main()