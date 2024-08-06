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

print("Welcome to Anne's Language Retreat\n")
print("Discover your level of English with our free online test.")
print("The test takes 10 - 15min to complete.")
print("Input the number (1 - 4) of the correct answer and press enter\n")

print("Example: What is the capital of France?\nA. Berlin\nB. Madrid\nC. Paris\nD. Rome")
# create input field for user answer
# check if user answered correctly
# check if user uses correct character

answer_example = int(input("Your answer (number): "))
if answer_example == 3:
    print("You are correct!")
elif answer_example < 4:
    print("Your answer is incorrect. The correct answer is Paris.")
else:
    print("Incorrect input. Please enter a number from 1 to 4")

print("Loading English Language test ...")

def ask_question(question, options, correct_option):
    """
    Prompts the user with a multiple-choice question
    """
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
    """
    Loads quiz data from the specified worksheet
    """
    questions_sheet = SHEET.worksheet('vocabulary')
    questions = questions_sheet.get_all_values()
    return questions

def calculate_score(questions):
    """
    Calculates the score based on user answers
    """
    score = 0
    for question in questions:
        correct = ask_question(
            question[0], 
            [question[1], question[2], question[3], question[4]], 
            question[5]
        )
        if correct:
            score += 1
        print(f"Current score: {score}")
    return score

def comprehension_quiz(sheet):
    text = sheet.cell(1, 1).value
    print(text)
    
    score = 0
    questions = sheet.get_all_records()[1:]
    
    for i in range(5):
        question = questions[i]
        print(f"Q{i+1}: {question[0]}")
        print(f"A: {question[1]}")
        print(f"B: {question[2]}")
        print(f"C: {question[3]}")
        print(f"D: {question[4]}")
        
        answer = input("Your answer: ").strip().upper()
        if answer == question['Correct']:
            score += 1
        print(f"Current score: {score}")
    
    return score

def main():
    # Load the quiz data (e.g., 5 questions from the 'vocabulary' worksheet)
    questions = load_quiz_data('vocabulary', 5)
    
    # Calculate the score based on the user's answers
    final_score = calculate_score(questions)
    
    # Display the final score
    print(f"\nYour final score is: {final_score} out of {len(questions)}")

    # Optionally run comprehension quiz
    comprehension_score = comprehension_quiz('comprehension')
    print(f"\nYour comprehension score is: {comprehension_score}")

if __name__ == "__main__":
    main()
