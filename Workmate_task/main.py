import argparse
import sys
from typing import List
from report_builder import ReportBuilder
from file_reader import read_employee_data, FileReadError


def main():
    # Настройка парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="Generate employee reports.")
    parser.add_argument("files", nargs="+", help="CSV files with employee data")
    parser.add_argument("--report", required=True, help="Type of report to generate")
    args = parser.parse_args()

    employees: List[dict] = []

    # Обрабатываем каждый переданный файл
    for file_path in args.files:
        try:
            employees.extend(read_employee_data(file_path))
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}", file=sys.stderr)
            sys.exit(1)
        except FileReadError as e:
            print(f"Error reading {file_path}: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error with {file_path}: {e}", file=sys.stderr)
            sys.exit(1)

    try:
        report = ReportBuilder.get_report(args.report, employees)
        print(report.generate())
    except ValueError as e:
        print(f"Report error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
