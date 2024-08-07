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

def sample_question():
    """
    Demonstrates to the user how to input their answers,
    checks if the user answered correctly,
    and ensures the user uses the correct character (numbers).
    """
    correct_answer = 3

    print("What is the capital of France?\n")
    
    options = ["Berlin", "Madrid", "Paris", "Rome"]
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Validate user input to ensure it's a number within the valid range
    while True:
        try:
            answer_example = int(input("Your answer (number): ").strip())
            if 1 <= answer_example <= 4:
                if answer_example == correct_answer:
                    print("You are correct!\n")
                else:
                    print(f"Your answer is incorrect. The correct answer is Paris.\n")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.\n")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.\n")

# Call the function
sample_question()

print("Loading English Language test ...\n")

def ask_question(question, options, correct_option):
    """
    Prompts the user with a multiple-choice question
    User request loop to repeat request for data until data provided is valid
    """
    print(f"\n{question}\n")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Your answer (number): "))
            if 1 <= answer <= len(options):
                return options[answer - 1] == correct_option
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def load_quiz_data(worksheet, num_questions):
    """
    Loads quiz data from the specified worksheet
    """
    questions_sheet = SHEET.worksheet(worksheet)
    questions = questions_sheet.get_all_values()
    return questions[1:num_questions + 1]

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
    """
    Prompts the user with a multiple-choice question
    User request loop to repeat request for data until data provided is valid
    """
    sheet = SHEET.worksheet('comprehension')
    
    # Get the reading text from cell A1 and display it
    text = sheet.cell(1, 1).value
    print(text)

    score = 0
    questions = sheet.get_all_records()[1:]
    
    for i in range(5):
        question = questions[i]
        print(f"\n{question['Question']}\n")
        print(f"1. {question['Option A']}")
        print(f"2. {question['Option B']}")
        print(f"3. {question['Option C']}")
        print(f"4. {question['Option D']}")
        
        while True:
            try:
                answer = int(input("Your answer (number): ").strip())
                if 1 <= answer <= 4:
                    if f"Option {chr(64 + answer)}" == question['Correct answer']:
                        score += 1
                    break
                else:
                    print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if answer == question['Correct answer']:
            score += 1
        print(f"Current score: {score}")
    
    return score

def determine_cefr_level(total_score):
    """

    """
    print(f"Total score: {total_score}")
    if total_score <= 10:
        return "A1 - Beginner"
    elif total_score <= 15:
        return "A2 - Elementary"
    elif total_score <= 20:
        return "B1 - Lower Intermediate"
    elif total_score <= 25:
        return "B2 - Upper Intermediate"
    elif total_score <= 30:
        return "C1 - Advanced"
    else:
        return "C2 - Proficiency"


def main():

    vocab_questions = load_quiz_data('vocabulary', 5)
    vocab_score = calculate_score(vocab_questions)
    
    grammar_questions = load_quiz_data('grammar', 5)
    grammar_score = calculate_score(grammar_questions)
    
    comprehension_score = comprehension_quiz(SHEET.worksheet('comprehension'))

    total_score = vocab_score + grammar_score + comprehension_score
    cefr_level = determine_cefr_level(total_score)

    print(f"\nQuiz Complete!")
    print(f"Vocabulary Section Score: {vocab_score}/15")
    print(f"Grammar Section Score: {grammar_score}/15")
    print(f"Text Comprehension Section Score: {comprehension_score}/5")
    print(f"Your CEFR Level is: {cefr_level}")


if __name__ == "__main__":
    main()
