class EmployeeSalary:
    hourly_payment = 400  # Почасовой уровень оплаты

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        if hours is not None:
            calculated_hours = hours
        elif rest_days is not None:
            calculated_hours = (7 - rest_days) * 8
        else:
            raise ValueError("Недостаточно данных для расчёта часов: не заданы ни hours, ни rest_days")

        return cls(name, calculated_hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            generated_email = f"{name}@email.com"
        else:
            generated_email = email

        return cls(name, hours, rest_days, generated_email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        """
        Изменяет почасовую ставку оплаты для всех сотрудников.

        Args:
            new_payment (float or int): новая почасовая ставка
        """
        cls.hourly_payment = new_payment

    def salary(self):
        """
        Рассчитывает заработную плату за неделю.

        Returns:
            float or int: заработная плата (часы * почасовая ставка)
        """
        if self.hours is None:
            raise ValueError("Часы работы не заданы и не могут быть рассчитаны")
        return self.hours * self.hourly_payment