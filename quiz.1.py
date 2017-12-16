import os
import time

def initiate_game():
    unused_variable = os.system("clear")
    prompt("Welcome to the Python Challenge!")
    prompt("See if you can fill in the blanks for each question when prompted.")
    time.sleep(2)
    unused_variable = os.system("clear")
    play_game(index,answers, questions, qnum)
    

def prompt(message):
    """
    This function adds an arrow to the left of the output.
    It is intended to help make prompts and instructions more readable.
    :inputs: the message as a string to which the arrow will be prepended.
    :outputs: a string containing the arrow and the game message will be printed.
    """
    print "=> " + message

def play_game(index, answers, questions, qnum):
    set_questions(questions, answers)
    while index < len(answers):
        ask_and_answer(questions, qnum)
        questions[index] = questions[index].replace("_____",answers[index])
        qnum += 1
        index += 1
# Question and answer loop ends here.
    for question in questions:
        print question
    print "\n"
    prompt("Congratulations on completing the challenge! <=" + "\n")

def set_difficulty():
    """
    This function prompts the user to enter their chosen difficulty level.
    :inputs: the function has no parameters.  It stores user input in the variable difficulty.
    :outputs: returns the value of the difficulty variable.
    """
    # time.sleep(1)
    prompt("Do you want an easy, medium, or hard challenge?")
    difficulty = raw_input("Type 'e', 'm', or 'h' => ")
    time.sleep(1)
    unused_variable = os.system("clear")
    return difficulty

def set_questions(questions, answers):
    """
    This function uses flow control to assign the correct variables to the
    questions and answers lists based on user difficulty selection.  It checks for
    valid user input to break the while loop or passes control back to ehte set_difficulty
    function in the case of invalid user input.
    :inputs: uses the return value of the set_difficulty function for comparison
    in the if statements.  The empty questions and answers lists are passed in as
    arguments.
    :outputs: the questions and answers with the appropriate variables added.
    If the user enters an invalid choice, the function prints an error message.
    """
    while True:
        difficulty = set_difficulty()
        if difficulty.lower() == 'e':
            questions += easy_questions
            answers += easy_answers
            break
        elif difficulty.lower() == 'm':
            questions += medium_questions
            answers += medium_answers
            break
        elif difficulty.lower() == 'h':
            questions += hard_questions
            answers += hard_answers
            break
        else:
            print "That isn't a valid difficulty level."
            time.sleep(1)
            unused_variable = os.system("clear")

def ask_and_answer(questions, qnum):
    """
    The function uses a for loop to print the selected list of questions
    and prompt the user for an answer to the current question.
    Invokes a call to the answer_check function.
    :inputs: the questions list for the appropriate difficulty level and the
    qnum variable to keep track of the current question number.
    :outputs: prints the questions and the prompt for the user to answer each question.
    Initiates a call to the answer_check function.
    """
    for question in questions:
        print question
    answer = raw_input("\n" + "What should go in the blank for QUESTION " + str(qnum) + "? ")
    answer_check(answer, answers, qnum, questions)


def answer_check(answer, answers, qnum, questions):
    """
    The function compares the user's answer to the expected answer.
    If correct, notifies user and returns to while loop in the main program.
    If not correct, notifies user and invokes the ask_and_answer function again.
    :inputs: requires the answer variable for the user's answer, the answers list to
    compare against, and the qnum variable to use for answer comparison.
    :outputs: prints message to user informing them whether they are correct or not.
    """
    if answer.lower() == answers[qnum - 1]:
        print "Correct! Great job!"
        time.sleep(1)
        unused_variable = os.system("clear")
        return
    else:
        print "Incorrect.  Please try again."
        time.sleep(1)
        unused_variable = os.system("clear")
        ask_and_answer(questions, qnum)

def close_game():
    prompt("Would you like to play again?")
    play_again = raw_input("Enter 'y' to play again or 'n' to quit. => ")
    if play_again.lower() == 'y':
        unused_variable = os.system("clear")
        return False
    else:
        print "Thanks for playing.  Have a great day!"
        time.sleep(1.5)
        unused_variable = os.system("clear")
        return True
        

# PROGRAM BEGINS HERE
# Outer loop allows user to play multiple games without restarting the program.
while True:
    easy_questions = [
        "1. Some number of characters surrounded by quotes is called a _____.",
        "2. A single line comment is preceded by this character: _____.",
        "3. This reserved word is used to start a function definition: _____.",
        "4. The position of an element within a List is called its _____."
    ]
         
    easy_answers = [
        "string",
        "#",
        "def",
        "index"
    ]
    
    medium_questions = [
        "1. A _____ loop iterates through each element in a list.",
        "2. An _____ is a test to make sure that the user input is valid.",
        "3. A variable in parentheses when defining a function is called a _____.",
        "4. A collection of elements within square brackets is called a _____."
    ]
    
    medium_answers = [
        "for",
        "assertion",
        "parameter",
        "list"
    ]
    
    hard_questions = [
        "1. The message showing a chain of steps leading to an error is a _____.",
        "2. Add to and reassign a variable in one step with the _____ operator.",
        "3. Objects that cannot be modified in place are referred to as _____.",
        "4. A _____ is a sequence of immutable objects that is like a list."
    ]
    
    hard_answers = [
        "traceback",
        "+=",
        "immutable",
        "tuple"    
    ]
    
    questions = []
    answers = []
    difficulty = ""
    index = 0
    qnum = 1
    
    initiate_game()

    # play_game(index,answers, questions, qnum)
    
    if close_game():
        break
