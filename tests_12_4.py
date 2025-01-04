#Задача "Логирование бегунов"

from unittest import TestCase
from test_code_2 import Runner
import logging


class RunnerTest(TestCase):
    def test_walk(self):
        try:
            runner = Runner('Name', -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('test_walk выполнен успешно')
        except Exception as e:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            runner = Runner(15)
            if not isinstance(runner.name, str):
                raise TypeError
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('test_run выполлнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner')

    def test_challengee(self):
        runner_1 = Runner('Володя')
        runner_2 =  Runner('Михалыч')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    logging.basicConfig(level = 'INFO', filemode = 'w', filename = 'runner_tests.log', coding = 'UTF - 8',
                        format = ' %(levelname) | %(message)')
    unittest.main()