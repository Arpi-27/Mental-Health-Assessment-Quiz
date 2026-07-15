QUESTIONS = [
    {
        "question": "1. How often do you feel overwhelmed?",
        "options": {
            "a": "Rarely",
            "b": "Sometimes",
            "c": "Often",
            "d": "Almost always",
        },
    },
    {
        "question": "2. How well are you sleeping lately?",
        "options": {
            "a": "Very well",
            "b": "Okay",
            "c": "Poorly",
            "d": "Barely sleeping",
        },
    },
    {
        "question": "3. How often do you feel anxious or nervous?",
        "options": {
            "a": "Rarely",
            "b": "Sometimes",
            "c": "Often",
            "d": "Almost always",
        },
    },
    {
        "question": "4. Do you find joy in activities you used to enjoy?",
        "options": {
            "a": "Yes, always",
            "b": "Most of the time",
            "c": "Sometimes",
            "d": "Rarely or never",
        },
    },
    {
        "question": "5. Do you feel connected to others?",
        "options": {
            "a": "Very connected",
            "b": "Somewhat connected",
            "c": "Isolated sometimes",
            "d": "Very isolated",
        },
    },
    {
        "question": "6. How is your appetite?",
        "options": {
            "a": "Normal",
            "b": "Slightly reduced",
            "c": "Poor",
            "d": "No appetite or overeating",
        },
    },
    {
        "question": "7. How often do you feel hopeless or down?",
        "options": {
            "a": "Never",
            "b": "Occasionally",
            "c": "Frequently",
            "d": "Almost always",
        },
    },
    {
        "question": "8. Are you able to concentrate on tasks?",
        "options": {
            "a": "Always",
            "b": "Usually",
            "c": "Sometimes",
            "d": "Rarely",
        },
    },
    {
        "question": "9. How often do you feel tired or low on energy?",
        "options": {
            "a": "Rarely",
            "b": "Sometimes",
            "c": "Often",
            "d": "Every day",
        },
    },
    {
        "question": "10. How often do you feel like you are not good enough?",
        "options": {
            "a": "Never",
            "b": "Rarely",
            "c": "Often",
            "d": "Almost always",
        },
    },
    {
        "question": "11. Do you often feel irritated or angry?",
        "options": {
            "a": "No",
            "b": "Occasionally",
            "c": "Often",
            "d": "Most of the time",
        },
    },
    {
        "question": "12. How well do you manage stress?",
        "options": {
            "a": "Very well",
            "b": "Moderately",
            "c": "Not well",
            "d": "Poorly",
        },
    },
    {
        "question": "13. Do you experience mood swings?",
        "options": {
            "a": "Rarely",
            "b": "Sometimes",
            "c": "Often",
            "d": "Very frequently",
        },
    },
    {
        "question": "14. How often do you feel lonely?",
        "options": {
            "a": "Never",
            "b": "Sometimes",
            "c": "Often",
            "d": "Almost always",
        },
    },
    {
        "question": "15. Do you worry about the future constantly?",
        "options": {
            "a": "No",
            "b": "Occasionally",
            "c": "Frequently",
            "d": "Always",
        },
    },
    {
        "question": "16. Do you avoid social situations?",
        "options": {
            "a": "Never",
            "b": "Sometimes",
            "c": "Often",
            "d": "Almost always",
        },
    },
    {
        "question": "17. Do you have trouble making decisions?",
        "options": {
            "a": "No",
            "b": "Occasionally",
            "c": "Often",
            "d": "Always",
        },
    },
    {
        "question": "18. Do you feel mentally exhausted?",
        "options": {
            "a": "Rarely",
            "b": "Sometimes",
            "c": "Often",
            "d": "Almost always",
        },
    },
    {
        "question": "19. Do you feel like a burden to others?",
        "options": {
            "a": "Never",
            "b": "Sometimes",
            "c": "Often",
            "d": "Always",
        },
    },
    {
        "question": "20. Are you finding it hard to stay motivated?",
        "options": {
            "a": "No",
            "b": "A little",
            "c": "Quite a bit",
            "d": "Yes, completely",
        },
    },
]


ANSWER_SCORES = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}


def get_result_message(total_score: int) -> str:
    """Return a general reflection message based on the total score."""

    if total_score <= 29:
        return (
            "You appear to be doing reasonably well. "
            "Continue maintaining healthy routines and support systems."
        )

    if total_score <= 49:
        return (
            "You may be experiencing some emotional challenges. "
            "Consider self-care and speaking with someone you trust."
        )

    if total_score <= 69:
        return (
            "Your answers suggest substantial stress. "
            "Consider speaking with a qualified mental-health professional."
        )

    return (
        "Your answers suggest serious distress. Please contact a qualified "
        "mental-health professional or a trusted support person promptly."
    )


def mental_health_quiz() -> int:
    """Run the command-line quiz and return the final score."""

    print("\nMental Health Reflection Quiz")
    print("This quiz is for reflection only and is not a medical diagnosis.\n")

    total_score = 0

    for question in QUESTIONS:
        print(f"\n{question['question']}")

        for key, option in question["options"].items():
            print(f"  {key}) {option}")

        while True:
            answer = input("Your answer (a/b/c/d): ").strip().lower()

            if answer in ANSWER_SCORES:
                total_score += ANSWER_SCORES[answer]
                break

            print("Invalid input. Please choose a, b, c, or d.")

    print(f"\nYour total score: {total_score}")
    print(get_result_message(total_score))

    return total_score