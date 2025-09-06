# Quiz questions stored in a list of dictionaries
questions = [
    {
        "question": "What does CPU stand for?",
        "choices": [
            "A) Central Process Unit",
            "B) Central Processing Unit",
            "C) Computer Personal Unit",
            "D) Central Processor Utility"
        ],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": [
            "A) def",
            "B) func",
            "C) define",
            "D) function"
        ],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": [
            "A) Earth",
            "B) Mars",
            "C) Jupiter",
            "D) Venus"
        ],
        "answer": "B"
    }
]

score = 0  # to track correct answers

# Loop through each question
for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for choice in q["choices"]:
        print(choice)

    answer = input("Your answer (A/B/C/D): ").upper()

    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.")

    print("-" * 30)

# Show final score
print("\nQuiz Finished!")
print(f"Your final score is {score}/{len(questions)}")
