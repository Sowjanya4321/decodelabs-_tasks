def ask_question(question, answer):

    user_answer = input(question + " ").strip().lower()

    if user_answer == answer.lower():
        print("✅ Correct!\n")
        return 1
    else:
        print(f"❌ Wrong! Correct Answer: {answer}\n")
        return 0


while True:

    score = 0

    print("\n====================================")
    print("      GENERAL KNOWLEDGE QUIZ")
    print("====================================")

    name = input("Enter Your Name: ")

    questions = [
        ("1. What is the capital of France?", "Paris"),
        ("2. Which planet is called the Red Planet?", "Mars"),
        ("3. Who invented Python?", "Guido van Rossum"),
        ("4. Which is the largest ocean in the world?", "Pacific Ocean"),
        ("5. How many continents are there?", "7"),
        ("6. What is the national animal of India?", "Tiger"),
        ("7. Which country is famous for the Eiffel Tower?", "France"),
        ("8. What is the square root of 64?", "8"),
        ("9. Who is known as the Father of the Nation in India?", "Mahatma Gandhi"),
        ("10. Which gas do plants absorb from atmosphere?", "Carbon Dioxide")
    ]

    review = []

    for q, a in questions:

        user_ans = input(q + " ").strip()

        if user_ans.lower() == a.lower():

            print("✅ Correct!\n")
            score += 1

        else:

            print(f"❌ Wrong! Correct Answer: {a}\n")

            review.append({
                "question": q,
                "your_answer": user_ans,
                "correct_answer": a
            })

    percentage = (score / len(questions)) * 100

    print("\n====================================")
    print("            FINAL RESULT")
    print("====================================")

    print(f"Player Name : {name}")
    print(f"Score       : {score}/{len(questions)}")
    print(f"Percentage  : {percentage:.2f}%")

    if percentage >= 90:
        grade = "A+"
        remark = "🏆 Outstanding"
    elif percentage >= 75:
        grade = "A"
        remark = "🎉 Excellent"
    elif percentage >= 60:
        grade = "B"
        remark = "👍 Good"
    elif percentage >= 40:
        grade = "C"
        remark = "🙂 Average"
    else:
        grade = "F"
        remark = "📚 Need Improvement"

    print(f"Grade       : {grade}")
    print(f"Remark      : {remark}")

    print("\n====================================")
    print("      ANSWER REVIEW SECTION")
    print("====================================")

    if len(review) == 0:
        print("🎯 Perfect Score! No mistakes.")
    else:

        for i, item in enumerate(review, start=1):

            print(f"\n{i}. {item['question']}")
            print(f"Your Answer    : {item['your_answer']}")
            print(f"Correct Answer : {item['correct_answer']}")

    print("\n====================================")

    play_again = input("Play Again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("\n👋 Thank you for playing the quiz!")
        break