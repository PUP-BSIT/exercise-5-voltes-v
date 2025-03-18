def quiz():
    score = 0
    total_questions = 6 #pag magdadagdag kayo ng question, magplus 1 kayo here

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
    print("\n(Dyanna) TRIVIA! What is my favorite color?")
    print("a) Blue")
    print("b) Red")
    print("c) Green")
    print("d) Purple")

    answer = input("Enter your answer: ").strip().lower()

    if answer == 'd':
        print("Correct!")
        score += 1
    else:
        print(f"{answer.upper()} is incorrect. The correct answer is D.")

    # Question 4
    print("\n(Dyanna) Fill in the blank for the song 'Oceans and Engines' by NIKI:")
    print('"Heaven _______ Destiny\'s _______"')
    print("a) Granted, Guide")
    print("b) Denied, Decried")
    print("c) Blessed, Tide")
    print("d) Lost, Light")

    answer = input("Enter your answer: ").strip().lower()

    if answer == 'b':
        print("Correct!")
        score += 1

    else:
        print(f"{answer.upper()} is incorrect. The correct answer is B.")

     # Question 5
    print("\n(JC) What will be the output of the following code?")
    print("age = '25'\nnew_age = int(age) + 5\nprint(new_age)")
    print("a) 25")
    print("b) '30'")
    print("c) 30")
    print("d) TypeError")

    answer = input("Enter your answer: ").strip().lower()
    if answer == 'c':
        print("Correct!")
        score += 1
    else:
        print(f"{answer.upper()} is incorrect. The correct answer is C.")

    # Question 6 
    print("\n(JC) Which logical operator returns True if at least one of the conditions is True?")
    print("a) or")
    print("b) and")
    print("c) not")
    print("d) xor")

    answer = input("Enter your answer: ").strip().lower()
    if answer == 'a':
        print("Correct!")
        score += 1
    else:
        print(f"{answer.upper()} is incorrect. The correct answer is A.")

    # Display Final Score
    print(f"\nCongratulations! You got {score} out of {total_questions} items.")

# Run the quiz
quiz()
