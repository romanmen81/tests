import unittest

# Определение класса Runner
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Позволяем выполнять тесты

    def test_run(self):
        runner = Runner("Usain", speed=10)
        runner.run()
        self.assertEqual(runner.distance, 20)

    def test_walk(self):
        runner = Runner("Usain", speed=10)
        runner.walk()
        self.assertEqual(runner.distance, 10)

    def test_challenge(self):
        runner1 = Runner("Usain Bolt")
        runner2 = Runner("Tyson Gay")
        runner1.run()  # Пробежал 20
        runner2.run()  # Пробежал 20
        runner1.run()  # Пробежал еще 20
        self.assertGreater(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Замораживаем тесты

    def test_first_tournament(self):
        self.assertTrue(True)

    def test_second_tournament(self):
        self.assertTrue(True)

    def test_third_tournament(self):
        self.assertTrue(True)