import os
import time

def prompt(message):
    print "=> " + message

# Ask player to select difficulty and return the response
def set_difficulty():
    time.sleep(1)
    prompt("Do you want an easy, medium, or hard challenge?")
    difficulty = raw_input("Type 'e', 'm', or 'h' => ")
    return difficulty

# Initialize the correct list and element variables based on user difficulty selection.
def set_questions(difficulty, questions, answers):
    while True:
        difficulty = set_difficulty()
        if difficulty.lower() == 'e':
            questions += [eq1, eq2, eq3, eq4]
            answers += [ea1, ea2, ea3, ea4]
            break
        elif difficulty.lower() == 'm':
            questions += [mq1, mq2, mq3, mq4]
            answers += [ma1, ma2, ma3, ma4]
            break
        elif difficulty.lower() == 'h':
            questions += [hq1, hq2, hq3, hq4]
            answers += [ha1, ha2, ha3, ha4]
            break
        else:
            print "That isn't a valid difficulty level."

# Print the selected list of questions and saves user's answers
# Invoke a call to the answer_check function
def ask_and_answer(questions, qnum):
    for question in questions:
        print question
    answer = raw_input("\n" + "What should go in the blank for QUESTION " + str(qnum) + "? ")
    answer_check(answer, answers, qnum)

# Compare the user's answer to the list of correct answers.
#  If correct, notify user and return to while loop in the main program.
#  If not correct, notify user and invoke the ask_and_answer function again.
def answer_check(answer, answers, qnum):
    if answer.lower() in answers:
        print "Correct! Great job!"
        time.sleep(1)
        unused_variable = os.system("clear")
        return
    else:
        print "Incorrect.  Please try again."
        time.sleep(1)
        unused_variable = os.system("clear")
        ask_and_answer(questions, qnum)


# PROGRAM BEGINS HERE
# Outer loop allows user to play multiple games without restarting the program.
while True:
    time.sleep(1)
    unused_variable = os.system("clear")
    prompt("Welcome to the Python Challenge!")
    prompt("See if you can fill in the blanks for each question when prompted.")
    time.sleep(1)

    eq1 = "1. Some number of characters surrounded by quotes is called a _____."
    eq2 = "2. A single line comment is preceded by this character: _____."
    eq3 = "3. This reserved word is used to start a function definition: _____."
    eq4 = "4. The position of an element within a List is called its _____."
    mq1 = "1. A _____ loop iterates through each element in a list."
    mq2 = "2. An _____ is a test to make sure that the user input is valid."
    mq3 = "3. A variable in parentheses when defining a function is called a _____."
    mq4 = "4. A collection of elements within square brackets is called a _____."
    hq1 = "1. The message showing a chain of steps leading to an error is a _____."
    hq2 = "2. Add to and reassign a variable in one step with the _____ operator."
    hq3 = "3. Objects that cannot be modified in place are referred to as _____."
    hq4 = "4. A _____ is a sequence of immutable objects that is like a list."
    ea1 = "string"
    ea2 = "#"
    ea3 = "def"
    ea4 = "index"
    ma1 = "for"
    ma2 = "assertion"
    ma3 = "parameter"
    ma4 = "list"
    ha1 = "traceback"
    ha2 = "+="
    ha3 = "immutable"
    ha4 = "tuple"
    questions = []
    answers = []
    difficulty = ""

    set_questions(difficulty, questions, answers)
    unused_variable = os.system("clear")

    index = 0
    qnum = 1
    
# Initiates the question and answer loop.
# Loop breaks when all questions have been answered correctly.
    while index < len(answers):
        ask_and_answer(questions, qnum)
# Replaces blank in current question with correct answer.
        questions[index] = questions[index].replace("_____",answers[index])
        qnum += 1
        index += 1
# Question and answer loop ends here.

    prompt("Congratulations on completing the challenge!")
    prompt("Would you like to play again?")
    play_again = raw_input("Enter 'y' to play again or 'n' to quit. => ")
    if play_again.lower() != 'y':
        unused_variable = os.system("clear")
        print "Thanks for playing.  Have a great day!"
        time.sleep(1.5)
        unused_variable = os.system("clear")
        break
