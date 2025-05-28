from typing import List, Dict, Any
import re


# Кастомное исключение для ошибок чтения файла
class FileReadError(Exception):
    pass


def read_employee_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает данные сотрудников из CSV-файла и возвращает список словарей.
    Args:
        file_path (str): Путь к CSV-файлу
    Returns:
        List[Dict[str, Any]]: Список сотрудников, где каждый сотрудник представлен словарем
    """
    try:
        with open(file_path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        raise FileReadError(f"Could not read file: {e}")

    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]
    rate_aliases = {"hourly_rate", "rate", "salary"}
    rate_header = next((h for h in headers if h.lower() in rate_aliases), None)

    if not rate_header:
        raise FileReadError("No valid hourly rate column found")

    employees = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        if len(values) != len(headers):
            continue

        employee = dict(zip(headers, values))
        try:
            employee["hours_worked"] = float(employee["hours_worked"])
            employee["hourly_rate"] = float(employee[rate_header])
        except (ValueError, KeyError) as e:
            continue

        employees.append(employee)

    # Если не нашли ни одного валидного сотрудника
    if not employees:
        raise FileReadError("No valid employee data found")

    return employees