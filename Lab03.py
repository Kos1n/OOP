class Service:
    """Модель медичної послуги."""
    
    def __init__(self, name, duration_min):
        self.name = name
        self.duration_min = duration_min

    def show_service(self):
        """Повертає інформацію про послугу."""
        return f"{self.name} ({self.duration_min} хв)"


class Client:
    """Модель пацієнта (клієнта) медичного центру."""
    
    def __init__(self, full_name, phone):
        self.full_name = full_name
        self.phone = phone

    def show_client(self):
        """Повертає інформацію про клієнта."""
        return f"{self.full_name} (тел: {self.phone})"


class Appointment:
    """Модель запису на прийом із контрольованим доступом до статусу."""
    
    valid_statuses = {"підтверджено", "завершено", "скасовано"}
    created_count = 0  # Атрибут класу для підрахунку створених записів

    def __init__(self, number, time, service, client, status="підтверджено"):
        self.number = number
        self.time = time
        self.service = service  # Екземпляр класу Service
        self.client = client    # Екземпляр класу Client
        
        self._status = "підтверджено"  # Початкове значення перед викликом setter
        self.status = status           # Запис проходить через setter із перевіркою
        
        Appointment.created_count += 1

    @property
    def status(self):
        """Повертає поточний статус із захищеного внутрішнього поля."""
        return self._status

    @status.setter
    def status(self, value):
        """Дозволяє встановити лише допустимий статус."""
        if value not in self.valid_statuses:
            raise ValueError(f"Невідомий статус: {value}")
        self._status = value

    def show(self):
        """Повертає стислий опис запису."""
        return (
            f"Запис №{self.number} | Час: {self.time} | "
            f"Клієнт: {self.client.show_client()} | "
            f"Послуга: {self.service.show_service()} | Статус: {self.status}"
        )


def find_by_status(items, status):
    """Повертає список записів із заданим статусом."""
    return [item for item in items if item.status == status]


# Демонстрація роботи з об'єктами
if __name__ == "__main__":
    # Створюємо об'єкти послуг
    s1 = Service("Консультація терапевта", 30)
    s2 = Service("Консультація стоматолога", 45)
    s3 = Service("УЗД", 20)

    # Створюємо вигадані об'єкти клієнтів (пацієнтів)
    c1 = Client("Григорій П.", "+380501112233")
    c2 = Client("Олена К.", "+380672223344")
    c3 = Client("Іван М.", "+380933334455")

    # Створюємо екземпляри записів
    appointments = [
        Appointment(1, "2026-10-29 09:00", s1, c1, "підтверджено"),
        Appointment(2, "2026-10-29 10:00", s2, c2, "завершено"),
        Appointment(3, "2026-10-29 11:30", s3, c3, "підтверджено")
    ]

    print("=== Усі записи медичного центру ===")
    for app in appointments:
        print(app.show())

    # Коректна зміна статусу через властивість (setter)
    appointments[0].status = "завершено"
    print("\n=== Після оновлення статусу першого запису ===")
    print(appointments[0].show())

    print("\n=== Вибірка записів зі статусом 'підтверджено' ===")
    confirmed_appointments = find_by_status(appointments, "підтверджено")
    for app in confirmed_appointments:
        print(app.show())

    print(f"\nЗагалом створено об'єктів записів: {Appointment.created_count}")