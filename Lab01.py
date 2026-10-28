appointments = [
    {
        "number": 1,
        "time": "2026-10-29 09:00",
        "service_name": "Консультація терапевта",
        "duration_min": 30,
        "status": "підтверджено"
    },
    {
        "number": 2,
        "time": "2026-10-29 10:00",
        "service_name": "Консультація стоматолога",
        "duration_min": 45,
        "status": "завершено"
    },
    {
        "number": 3,
        "time": "2026-10-29 11:30",
        "service_name": "УЗД",
        "duration_min": 20,
        "status": "підтверджено"
    }
]


def show_appointments(items):
    """Виводить номер, час, назву послуги, тривалість та статус кожного запису."""
    for item in items:
        print(
            f"Запис №{item['number']} | Час: {item['time']} | "
            f"Послуга: {item['service_name']} ({item['duration_min']} хв) | "
            f"Статус: {item['status']}"
        )


def find_by_status(items, status):
    """Повертає список записів із заданим статусом."""
    return [item for item in items if item["status"] == status]


# Демонстрація роботи прототипу
if __name__ == "__main__":
    print("=== Повний перелік записів у медичному центрі ===")
    show_appointments(appointments)

    print("\n=== Записи зі статусом 'підтверджено' ===")
    confirmed_appointments = find_by_status(appointments, "підтверджено")
    show_appointments(confirmed_appointments)