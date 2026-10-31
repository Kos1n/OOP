class Service:
    """Модель медичної послуги."""
    
    def __init__(self, name, duration_min):
        self.name = name
        self.duration_min = duration_min

    def show_service(self):
        """Повертає інформацію про послугу."""
        return f"{self.name} ({self.duration_min} хв)"


class Appointment:
    """Модель запису на прийом у медичному центрі."""
    
    valid_statuses = {"підтверджено", "завершено", "скасовано"}

    def __init__(self, number, time, service, status="підтверджено"):
        if status not in self.valid_statuses:
            raise ValueError("Невідомий статус")
        self.number = number
        self.time = time
        self.service = service  # Екземпляр класу Service
        self.status = status

    def show(self):
        """Повертає стислий опис запису."""
        return (
            f"Запис №{self.number} | Час: {self.time} | "
            f"Послуга: {self.service.show_service()} | Статус: {self.status}"
        )

    def change_status(self, status):
        """Змінює статус запису після його перевірки."""
        if status not in self.valid_statuses:
            raise ValueError("Невідомий статус")
        self.status = status


def show_appointments(items):
    """Виводить інформацію про кожен запис зі списку."""
    for item in items:
        print(item.show())


def find_by_status(items, status):
    """Повертає список записів із заданим статусом."""
    return [item for item in items if item.status == status]


# Демонстрація роботи з об'єктами
if __name__ == "__main__":
    # Створюємо об'єкти послуг
    s1 = Service("Консультація терапевта", 30)
    s2 = Service("Консультація стоматолога", 45)
    s3 = Service("УЗД", 20)

    # Створюємо об'єкти записів на основі вашого списку
    appointments = [
        Appointment(1, "2026-10-29 09:00", s1, "підтверджено"),
        Appointment(2, "2026-10-29 10:00", s2, "завершено"),
        Appointment(3, "2026-10-29 11:30", s3, "підтверджено")
    ]

    print("=== Повний перелік записів у медичному центрі ===")
    show_appointments(appointments)

    print("\n=== Записи зі статусом 'підтверджено' ===")
    confirmed_appointments = find_by_status(appointments, "підтверджено")
    show_appointments(confirmed_appointments)