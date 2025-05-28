from Workmate_task.report_builder import PayoutReport


def test_payout_report():
    employees = [
        {"department": "HR", "hours_worked": 318, "hourly_rate": 41.5},
        {"department": "Marketing", "hours_worked": 150, "hourly_rate": 35},
        {"department": "Design", "hours_worked": 170, "hourly_rate": 60},
    ]

    report = PayoutReport(employees)
    output = report.generate()

    # Проверяем, что заголовок присутствует
    assert "Отчёт по выплатам" in output
    assert "========================================" in output
    assert "Отдел           |       Часы |         Выплаты" in output
    assert "----------------------------------------" in output

    # Проверяем, что строки с данными присутствуют
    assert "HR" in output
    assert "318.0" in output
    assert "13197.00 ₽" in output
    assert "Marketing" in output
    assert "150.0" in output
    assert "5250.00 ₽" in output
    assert "Design" in output
    assert "170.0" in output
    assert "10200.00 ₽" in output

    # Проверяем, что итоговое количество сотрудников правильно
    assert "Итого сотрудников: 3" in output
