import csv
from pathlib import Path
from typing import Iterable


FIELD_NAMES = ["username", "score", "timestamp"]


def export_quiz_data(
    data: Iterable[dict],
    output_file: str | Path = "quiz_data.csv",
) -> Path:
    """Write quiz records to a CSV file and return its path."""

    output_path = Path(output_file)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(data)

    return output_path