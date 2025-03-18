def quiz():
    score = 0
    total_questions = 2 #pag magdadagdag kayo ng question, magplus 1 kayo here

    # Question 1
    print("(Precious) What is the primary purpose of a compiler?")
    print("a) To execute code directly")
    print("b) To translate high-level code into machine code")
    print("c) To debug code")
    print("d) To manage memory allocation")

    answer = input("Enter your answer: ").strip().lower()

    if answer == 'b':
        print("Correct!")
        score += 1
    else:
        print(f"{answer.upper()} is incorrect. The correct answer is B.")

    # Question 2
    print("\n(Precious) Which data structure operates on a First-In-First-Out (FIFO) principle?")
    print("a) Stack")
    print("b) Queue")
    print("c) Linked List")
    print("d) Tree")

    answer = input("Enter your answer: ").strip().lower()

    if answer == 'b':
        print("Correct!")
        score += 1
    else:
        print(f"{answer.upper()} is incorrect. The correct answer is B.")

    # Question 3
    print("\n(Name) Your Question")
    print("a) ")
    print("b) ")
    print("c) ")
    print("d) ")

    answer = input("Enter your answer: ").strip().lower()

    if answer == '*correct answer*':
        print("Correct!")
        score += 1
    else:
        print(f"{answer.upper()} is incorrect. The correct answer is *correct answer*.")


    # Display Final Score
    print(f"\nCongratulations! You got {score} out of {total_questions} items.")

# Run the quiz
quiz()
