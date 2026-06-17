class Results:
    def __init__(self, victories, draws, losses):
        """
        Args:
            victories (int): количество побед
            draws (int): количество ничьих
            losses (int): количество поражений
        """
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"

    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"

    def total_points(self):
        """Рассчитывает общее количество очков для футбола: 3*победы + ничьи."""
        points = 3 * self.victories + self.draws
        return f"Общее количество очков: {points}"

class Hockey(Results):
    def number_of_wins(self):
        return f"Хоккейных побед: {self.victories}"

    def number_of_draws(self):
        return f"Хоккейных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Хоккейных поражений: {self.losses}"

    def total_points(self):
        points = 2 * self.victories + self.draws
        return f"Общее количество очков: {points}"

# Создаём объекты
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

# Список методов, которые нужно вызвать для каждого объекта
methods_to_call = [
    'number_of_wins',
    'number_of_draws',
    'number_of_losses',
    'total_points'
]

# Цикл по обоим командам
for team in (football_team, hockey_team):
    # Определяем тип команды для заголовка
    if isinstance(team, Football):
        print("=== Результаты футбольной команды ===")
    elif isinstance(team, Hockey):
        print("\n=== Результаты хоккейной команды ===")

    # Вызываем все методы для текущей команды
    for method_name in methods_to_call:
        method = getattr(team, method_name)
        print(method())