import json

def load_questions(filename="quiz_data.json"):
    """
    Loads quiz questions from a JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

def run_quiz(questions):
    """
    Runs the quiz, calculates the score, and returns it.
    """
    score = 0
    for i, item in enumerate(questions):
        print(f"\nQuestion {i + 1}: {item['question']}")
        for j, option in enumerate(item['options']):
            print(f"  {j + 1}. {option}")
        
        while True:
            try:
                user_choice = int(input("Enter your choice (1-4): "))
                if 1 <= user_choice <= 4:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        user_answer = item['options'][user_choice - 1]
        if user_answer == item['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {item['answer']}.")
            
    return score

def main():
    """
    Main function to run the quiz application.
    """
    questions = load_questions()
    total_questions = len(questions)
    
    print("Welcome to the Online Quiz Platform!")
    
    score = run_quiz(questions)
    
    print("\n--- Quiz Finished ---")
    print(f"Your final score is: {score}/{total_questions}")
    print(f"You got {score} out of {total_questions} questions correct.")

if __name__ == "__main__":
    main()
