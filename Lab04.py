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
    """Базова модель запису на прийом із контрольованим доступом до статусу."""
    
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
        """Повертає загальну інформацію про запис."""
        return (
            f"Запис №{self.number} | Час: {self.time} | "
            f"Клієнт: {self.client.show_client()} | "
            f"Послуга: {self.service.show_service()} | Статус: {self.status}"
        )


class Consultation(Appointment):
    """Похідний клас для консультаційних прийомів лікаря."""

    def __init__(self, number, time, service, client, doctor_office, status="підтверджено"):
        # Ініціалізація базових атрибутів через конструктор базового класу
        super().__init__(number, time, service, client, status)
        self.doctor_office = doctor_office  # Специфічне поле: номер кабінету лікаря

    def get_consultation_details(self):
        """Повертає специфічну інформацію для консультації."""
        return f"Консультація проводиться в кабінеті №{self.doctor_office}"


class DiagnosticVisit(Appointment):
    """Похідний клас для діагностичних процедур (УЗД, аналізи тощо)."""

    def __init__(self, number, time, service, client, equipment_code, status="підтверджено"):
        # Ініціалізація базових атрибутів через конструктор базового класу
        super().__init__(number, time, service, client, status)
        self.equipment_code = equipment_code  # Специфічне поле: інвентарний код обладнання

    def get_diagnostic_details(self):
        """Повертає специфічну інформацію для діагностики."""
        return f"Використовується обладнання з кодом: {self.equipment_code}"


def find_by_status(items, status):
    """Повертає список записів із заданим статусом."""
    return [item for item in items if item.status == status]


# Демонстрація роботи з ієрархією класів
if __name__ == "__main__":
    # Створюємо об'єкти послуг
    s1 = Service("Консультація терапевта", 30)
    s2 = Service("УЗД черевної порожнини", 40)

    # Створюємо вигадані об'єкти клієнтів
    c1 = Client("Олександр Т.", "+380501112233")
    c2 = Client("Марія Д.", "+380672223344")

    # Створюємо екземпляри похідних класів
    consultation_app = Consultation(
        number=1, 
        time="2026-10-29 09:00", 
        service=s1, 
        client=c1, 
        doctor_office="204", 
        status="підтверджено"
    )
    
    diagnostic_app = DiagnosticVisit(
        number=2, 
        time="2026-10-29 10:30", 
        service=s2, 
        client=c2, 
        equipment_code="EQ-9988", 
        status="підтверджено"
    )

    appointments = [consultation_app, diagnostic_app]

    print("=== Усі записи медичного центру (з використанням успадкування) ===")
    for app in appointments:
        print(app.show())
        # Викликаємо специфічні методи нащадків залежно від типу об'єкта
        if isinstance(app, Consultation):
            print(f"   -> {app.get_consultation_details()}")
        elif isinstance(app, DiagnosticVisit):
            print(f"   -> {app.get_diagnostic_details()}")
        print("-" * 50)

    # Перевірка роботи властивості (setter) для контрольованої зміни статусу
    consultation_app.status = "завершено"
    print(f"\nСтатус першого запису після оновлення: {consultation_app.status}")
    print(f"Загалом створено записів: {Appointment.created_count}")