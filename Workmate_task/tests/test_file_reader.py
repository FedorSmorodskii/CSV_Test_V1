import os
import tempfile
from Workmate_task.file_reader import read_employee_data


def test_read_employee_data():
    csv_content = """id,email,name,department,hours_worked,rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
3,carol@example.com,Carol Williams,Design,170,60"""

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(csv_content)
        f.close()

        employees = read_employee_data(f.name)
        os.unlink(f.name)

        assert len(employees) == 3
        assert employees[0]["name"] == "Alice Johnson"
        assert employees[0]["hours_worked"] == 160.0
        assert employees[0]["hourly_rate"] == 50.0