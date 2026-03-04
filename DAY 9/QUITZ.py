def run_quiz():
    questions = [
        {
            "question": "1. Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. define"],
            "answer": "B"
        },
        {
            "question": "2. Which data type is used to store text in Python?",
            "options": ["A. int", "B. float", "C. str", "D. char"],
            "answer": "C"
        },
        {
            "question": "3. What symbol is used to start a comment in Python?",
            "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
            "answer": "C"
        },
        {
            "question": "4. Which function is used to get user input in Python?",
            "options": ["A. input()", "B. scan()", "C. read()", "D. gets()"],
            "answer": "A"
        },
        {
            "question": "5. What is the output of: print(type(10))?",
            "options": ["A. <class 'float'>", "B. <class 'str'>", "C. <class 'int'>", "D. <class 'bool'>"],
            "answer": "C"
        },
        {
            "question": "6. Which operator is used for exponentiation in Python?",
            "options": ["A. ^", "B. **", "C. *", "D. //"],
            "answer": "B"
        },
        {
            "question": "7. Which of these is a valid variable name?",
            "options": ["A. 2value", "B. value-2", "C. value_2", "D. value 2"],
            "answer": "C"
        },
        {
            "question": "8. What will print(3 == 3) output?",
            "options": ["A. True", "B. False", "C. 3", "D. Error"],
            "answer": "A"
        },
        {
            "question": "9. Which loop is used when the number of iterations is known?",
            "options": ["A. while", "B. do-while", "C. for", "D. loop"],
            "answer": "C"
        },
        {
            "question": "10. Which keyword is used to stop a loop in Python?",
            "options": ["A. exit", "B. stop", "C. break", "D. end"],
            "answer": "C"
        }
    ]

    score = 0
    print("\n🐍 Welcome to the Python Basics Quiz!\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"🎉 Quiz completed! Your score: {score}/10")


run_quiz()
