score = 0 #initializing the score to 0
questions = [
    {"question": "What is the capital of India?", "answer": "Delhi"},
    {"question": "2 + 2 = ?", "answer": "4"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the largest ocean?", "answer": "Pacific"},
    {"question": "Who wrote Harry Potter?", "answer": "J.K. Rowling"}
]
for q in questions:
    ans = input(q["question"] + " ")
    if ans.strip().lower() == q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer is:", q["answer"])

print("\nYour final score is:", score, "out of", len(questions))
