class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0  
        if place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0 

        return 101 - place

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0  # Всегда возвращаем числовой тип
        return meters * 0.5

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()

    def get_total_points(self, meters, place):
        points_for_place = self.get_points_for_place(place)
        points_for_meters = self.get_points_for_meters(meters)
        total = points_for_place + points_for_meters
        return int(total)  # Приводим результат к целому числу

# Тестирование
print(PointsForPlace.get_points_for_place(10))  # 91
print(PointsForMeters.get_points_for_meters(10))  # 5.0

total_points = TotalPoints()
print(total_points.get_points_for_place(10))  # 91
print(total_points.get_points_for_meters(10))  # 5.0
print(total_points.get_total_points(100, 10))  # 141 (целое число)
print(total_points.get_total_points(-5, 150))  # 0 (ошибки → 0)