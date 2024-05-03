"""Python quiz from json files for L1DISC 1.1"""

# Import the necessary libraries.
import os
import time
import json
import random

# Function to print a buffer of lines (used for looks).
def print_buffer(lines):
    print("\n" * lines)

# Check if the terminal is large enough to display the quiz nicely.
def check_terminal_size():
    if (
        os.get_terminal_size().columns < 100
        or os.get_terminal_size().lines < 20
    ):
        print("Terminal too small")
        exit()

# Load quiz data fron json files in the questions folder.
def load_quizzes():
    quizzes = {}
    current_dir = os.path.dirname(os.path.realpath(__file__))
    questions_dir = os.path.join(current_dir, "questions")
    for filename in os.listdir(questions_dir):
        if filename.endswith(".json"):
            with open(os.path.join(questions_dir, filename)) as json_data:
                quizzes[os.path.splitext(filename)[0]] = json.load(json_data)
    for question in quizzes: # print the loaded questions
        print(f'Loaded {question}:\nName: {quizzes[question]["config"]["name"]}\n')
    return quizzes
# Ask user to select a quiz or exit the program.
def quiz_selection(quizzes):
    os.system("clear")
    print_buffer(5)
    print('Select a quiz or type "quit" to exit:\n')
    quiz_dict = {}
    for question in quizzes:
        print(f'{question}: {quizzes[question]["config"]["name"]}')
        quiz_dict[quizzes[question]["config"]["name"].lower()] = question
    print("quit: Exit the program")
    quiz = input("\nQuiz: ")
    if quiz.lower() == "quit":
        os.system("clear")
        exit()
    elif quiz.lower() in quizzes:
        os.system("clear")
        return quiz
    elif quiz.lower() in quiz_dict:
        os.system("clear")
        return quiz_dict[quiz]
    return quiz_selection(quizzes)

# Display the quiz instructions and start the quiz.
def instructions(quiz, quizzes):
    os.system("clear")
    print_buffer(2)
    config = quizzes[quiz]["config"]
    print(
        f"{config['name']}\n{config['description']}\nAuthor: {config['author']}"
    )
    print_buffer(2)
    print(
        "Instructions:\nAnswer questions by typing the answer",
        "and pressing enter"
    )
    input("Press enter to start")
    os.system("clear")
    return quiz

# Function to run quiz.
def start_quiz(quiz, quizzes):
    
    # Function to print answer after user input.
    def print_answer(status, question, correct_answer):
        if status:
            os.system("clear")
            print_buffer(2)
            print(question)
            print("Correct")
            print_buffer(2)
            input("Press enter to continue")
        else:
            os.system("clear")
            print_buffer(2)
            print(question)
            print("Incorrect")
            print_buffer(2)
            print(f"Correct Answer: {correct_answer}")
            print_buffer(2)
            input("Press enter to continue")
            
    # Setup quiz and shuffle questions if required.        
    points = 0
    if quizzes[quiz]["config"]["shuffle"]:
        random.shuffle(quizzes[quiz]["questions"])
        
    # Loop through questions.  
    for question in quizzes[quiz]["questions"]:
        
        # Display question and options.
        os.system("clear")
        print(f"Score: {points}/{len(quizzes[quiz]['questions'])}")
        print_buffer(2)
        print(f"{question['question']}\n")

        # Handle single choice questions.
        if question["type"] == "choice":
            choices = question["incorrect"] + [question["correct"]]
            random.shuffle(choices)
            for index, choice in enumerate(choices):
                print(f"{index + 1}: {choice}")
            while True:  # get answer from user (loop if invalid input)
                answer = input("\nAnswer: ").lower()
                if answer == question["correct"].lower():  # check if answer is correct
                    print_answer(True, question["question"], question["correct"])
                    points += 1
                    break
                try:  # check if answer is correct corresponding number
                    answer = int(answer)
                    if 1 <= answer <= len(choices):
                        if choices[answer - 1].lower() == question["correct"].lower():
                            print_answer(True, question["question"], question["correct"])
                            points += 1
                        else:
                            print_answer(False, question["question"], question["correct"])
                        break
                    print(f"Enter a number between 1 and {len(choices)}")
                except ValueError:  # print error for invalid input
                    print("Enter a valid number.")
                    
        # Handle true/false questions.
        elif question["type"] == "truefalse":
            while True:
                answer = input("\nAnswer (true/false): ").lower()
                # Accept 't' and 'f' as valid inputs
                if answer in ['t', 'true']:
                    answer = True
                elif answer in ['f', 'false']:
                    answer = False
                else:
                    print("Invalid input. Please enter true/false or t/f.")
                    continue

                if answer == question["correct"]:
                    print_answer(True, question["question"], question["correct"])
                    points += 1
                else:
                    print_answer(False, question["question"], question["correct"])
                break

        # Handle short answer questions.
        elif question["type"] == "shortanswer":
            answer = input("\nAnswer: ").strip()
            if answer.lower() == question["correct"].lower():
                print_answer(True, question["question"], question["correct"])
                points += 1
            else:
                print_answer(False, question["question"], question["correct"])

    # print results with option to exit and to do antoher 
    # one and print the score with percentage and quiz name
    os.system("clear")
    print_buffer(2)
    print(f"Score: {points}/{len(quizzes[quiz]['questions'])}")
    print(f"Percentage: {points / len(quizzes[quiz]['questions']) * 100}%")
    print_buffer(2)
    input("Press enter to exit")
    # start a new quiz
    selected_quiz = quiz_selection(quizzes)
    instructions(selected_quiz, quizzes)
    start_quiz(selected_quiz, quizzes)

# Run the program.
os.system("clear")
check_terminal_size()
quizzes = load_quizzes()
selected_quiz = quiz_selection(quizzes)
instructions(selected_quiz, quizzes)
start_quiz(selected_quiz, quizzes)