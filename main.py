from mental_health.classifier import predict_score, train_classifier
from mental_health.csv_service import export_quiz_data
from mental_health.data import QUIZ_DATA
from mental_health.quiz import mental_health_quiz


def main() -> None:
    csv_path = export_quiz_data(QUIZ_DATA)
    print(f"Data written to {csv_path}")

    result = train_classifier(QUIZ_DATA)

    print(f"\nModel accuracy: {result.accuracy:.2f}")
    print("\nClassification report:")
    print(result.report)

    predicted_class = predict_score(result.model, 56)
    print(f"Predicted class for score 56: {predicted_class}")

    mental_health_quiz()


if __name__ == "__main__":
    main()