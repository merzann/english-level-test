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



def ask_question(question, options, correct_option):
    """
    Prompts the user with a multiple-choice question
    """
    print("Welcome to Anne'\s Language Retreat\n")
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

def load_quiz_data(worksheet, num_questions):
    questions_sheet = SHEET.worksheet('vocabulary')
    questions = questions_sheet.get_all_values()
    score = 0
    for i in range(num_questions):
        question = questions[i]
        correct = ask_question(
            question[0], 
            [question[1], question[2], question[3], question[4]], 
            question[5]
        )
        if correct:
            score += 1
        print(f"Current score: {score}")
    return score

load_quiz_data(SHEET, 5)