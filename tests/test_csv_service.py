import csv

from mental_health.csv_service import export_quiz_data


def test_export_quiz_data(tmp_path) -> None:
    sample_data = [
        {
            "username": "Test User",
            "score": 42,
            "timestamp": "2025-04-21 09:48",
        }
    ]

    output_file = tmp_path / "quiz_data.csv"

    created_file = export_quiz_data(sample_data, output_file)

    assert created_file.exists()

    with created_file.open(encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 1
    assert rows[0]["username"] == "Test User"
    assert rows[0]["score"] == "42"