import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Начальное количество врагов
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)  # Задержка 1 секунда
            self.days += 1
            self.enemies -= self.power

            if self.enemies < 0:
                self.enemies = 0  # Убедимся, что количество врагов не уходит в отрицательное

            day_word = "дней" if self.days > 1 else "день"
            print(f"{self.name}, сражается {self.days} {day_word}..., осталось {self.enemies} воинов.")

        # Победа
        print(f"{self.name} одержал победу спустя {self.days} {day_word}!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

# Сообщение об окончании
print("Все битвы закончились!")