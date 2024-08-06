import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('english_level_test')

def test_ask_question():
    question = "What is the capital of France?"
    options = ["Berlin", "Madrid", "Paris", "Rome"]
    correct_option = "Paris"
    
    # Call the ask_question function with the test data
    result = ask_question(question, options, correct_option)
    
    # Print the result to verify if it works correctly
    print(f"Result: {result}")

def ask_question(question, options, correct_option):
    """
    Prompts the user with a multiple-choice question
    """
    print(f"Welcome to Anne'\s Language Retreat\n")
    print("Discover your level of English with our free online test")
    print("This test takes 10 - 15min to complete.")
    print("Input the letter (A - D) of the correct answer and press enter\n")
    print("Example: What is the capital of France?\nA. Berlin\nB. Madrid\nC. Paris\nD. Rome\nYour answer (letter A-D): C\n")

    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Your answer (number): "))
            if 1 <= answer <= len(options):
                print(f"Answer received: {answer}")
                return options[answer - 1] == correct_option
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

test_ask_question()