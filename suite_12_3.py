import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Декоратор для пропуска тестов
def skip_if_frozen(method):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return method(self)
    return wrapper

# Обновляем методы в классе, чтобы использовать декоратор
def decorate_tests(test_class):
    for name in dir(test_class):
        if name.startswith("test_"):
            method = getattr(test_class, name)
            setattr(test_class, name, skip_if_frozen(method))

decorate_tests(RunnerTest)  # Декорируем тесты RunnerTest
decorate_tests(TournamentTest)  # Декорируем тесты TournamentTest

# Создаем тестовый набор
loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

# Запуск тестов
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)