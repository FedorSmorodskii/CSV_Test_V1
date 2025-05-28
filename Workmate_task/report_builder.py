from typing import List, Dict, Any, Protocol, runtime_checkable


@runtime_checkable
class Report(Protocol):
    def generate(self) -> str:
        """Generates the report output."""
        ...


class PayoutReport:
    def __init__(self, employees: List[Dict[str, Any]]):
        self.employees = employees

    def generate(self) -> str:
        report_lines = ["Отчёт по выплатам", "=" * 40]
        report_lines.append(f"{'Отдел':<15} | {'Часы':>10} | {'Выплаты':>15}")
        report_lines.append("-" * 40)

        departments = {}

        for emp in self.employees:
            dept = emp.get("department", "Не указано")  # Используем get для безопасного доступа
            hours = emp.get("hours_worked", 0)  # Значение по умолчанию
            payout = hours * emp.get("hourly_rate", 0)  # Значение по умолчанию

            if dept in departments:
                departments[dept]["hours"] += hours
                departments[dept]["payout"] += payout
            else:
                departments[dept] = {"hours": hours, "payout": payout}

        for dept, data in departments.items():
            report_lines.append(
                f"{dept:<15} | {data['hours']:>10.1f} | {data['payout']:>15.2f} ₽"
            )

        report_lines.append("=" * 40)
        report_lines.append(f"Итого сотрудников: {len(self.employees)}")

        return "\n".join(report_lines)


class AverageRateReport:
    def __init__(self, employees: List[Dict[str, Any]]):
        self.employees = employees

    def generate(self) -> str:
        avg_rate = sum(e["hourly_rate"] for e in self.employees) / len(self.employees)
        return f"Average Hourly Rate: {avg_rate:.2f}"


class ReportBuilder:
    _reports = {
        "payout": PayoutReport,
        "avg_rate": AverageRateReport,
    }

    @classmethod
    def get_report(cls, report_type: str, employees: List[Dict[str, Any]]) -> Report:
        if report_type not in cls._reports:
            raise ValueError(f"Unsupported report type: {report_type}")
        return cls._reports[report_type](employees)

class DepartmentSizeReport:
    def __init__(self, employees: List[Dict[str, Any]]):
        self.employees = employees

    def generate(self) -> str:
        dept_counts = {}
        for emp in self.employees:
            dept = emp["department"]
            dept_counts[dept] = dept_counts.get(dept, 0) + 1
        return "\n".join([f"{dept}: {count}" for dept, count in dept_counts.items()])

