from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def classify_score(score: int) -> str:
    """Convert a numerical score into a mental-health concern category."""

    if score >= 70:
        return "High"

    if score >= 40:
        return "Medium"

    return "Low"


@dataclass
class ModelResult:
    model: DecisionTreeClassifier
    accuracy: float
    report: str


def train_classifier(data: list[dict]) -> ModelResult:
    """Train and evaluate a decision-tree classifier."""

    dataframe = pd.DataFrame(data)
    dataframe["class"] = dataframe["score"].apply(classify_score)

    features = dataframe[["score"]]
    labels = dataframe["class"]

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=0.4,
        random_state=42,
        stratify=labels,
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    return ModelResult(
        model=model,
        accuracy=accuracy_score(y_test, predictions),
        report=classification_report(
            y_test,
            predictions,
            zero_division=0,
        ),
    )


def predict_score(model: DecisionTreeClassifier, score: int) -> str:
    """Predict a category for one score."""

    input_data = pd.DataFrame({"score": [score]})
    prediction = model.predict(input_data)

    return str(prediction[0])