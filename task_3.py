class PointsForPlace:
    def __init__(self):
        self.points = 0  # Изначально количество очков равно нулю

    def get_points_for_place(self, place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return None
        if place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return None

        points = 101 - place
        return points

class PointsForMeters:
    def __init__(self):
        self.points = 0  # Изначально количество очков равно нулю

    def get_points_for_meters(self, meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return None

        points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса

    def get_total_points(self, meters, place):
        points_for_place = self.get_points_for_place(place)
        points_for_meters = self.get_points_for_meters(meters)

        # Если какой‑то из методов вернул None, возвращаем 0 как целое число
        if points_for_place is None or points_for_meters is None:
            return 0

        total = points_for_place + points_for_meters
        return int(total)  # Приводим результат к целому числу

# Тестирование
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))  # 91

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))  # 5.0

total_points = TotalPoints()
print(total_points.get_points_for_place(10))  # 91
print(total_points.get_points_for_meters(10))  # 5.0
print(total_points.get_total_points(100, 10))  # 141 (целое число)
print(total_points.get_total_points(-5, 150))  # 0 (ошибки → 0)