import pytest

from mental_health.classifier import classify_score


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (0, "Low"),
        (39, "Low"),
        (40, "Medium"),
        (69, "Medium"),
        (70, "High"),
        (80, "High"),
    ],
)
def test_classify_score(score: int, expected: str) -> None:
    assert classify_score(score) == expected