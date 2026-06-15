class PointsForPlace:
    def __init__(self):
        self.points = 0  # Изначально количество очков равно нулю

    @staticmethod
    def get_points_for_place(place):
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

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return None

        points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса

    @staticmethod
    def get_total_points(meters, place):
        points_for_place = PointsForPlace.get_points_for_place(place)
        points_for_meters = PointsForMeters.get_points_for_meters(meters)

        if points_for_place is None or points_for_meters is None:
            return None

        total = points_for_place + points_for_meters
        return total

# Тестирование
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))  # 91

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))  # 5.0

total_points = TotalPoints()
print(total_points.get_points_for_place(10))  # 91
print(total_points.get_points_for_meters(10))  # 5.0
print(total_points.get_total_points(100, 10))  # 141.0