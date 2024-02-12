import random

# Define the quiz questions and answers
quiz_questions = {
    'Programming': {
        'What does the len() function do in Python?': ['A. Returns the length of a list, tuple, or string',
                                                       'B. Returns the length of a string.',
                                                       'C. Returns the logarithm of a number'],

        'What is the output of x = 5 y = 2 print(x ** y)': ['A. 25', 'B. 7', 'C. 10'],
        'my_list = [1, 2, 3, 4, 5]  print(my_list[2:])': ['A. [3, 4, 5]', 'B. [2, 3, 4, 5]', 'C. [1,2]']
    },

    'SQL': {
        'What does SQL stand for?': ['A. Structured Query Language', 'B. Simple Query Language',
                                     'C. Structured Question Language'],
        'Which SQL command is used to retrieve data from a database?': ['A. SELECT', 'B. UPDATE', 'C. INSERT INTO'],
        'Which SQL keyword is used to add new rows to a table?': ['A. INSERT INTO', 'B. CREATE', 'C. ALTER']
    },

    'Web Technologies': {
        'What does HTML stand for?': ['A. HyperText Markup Language', 'B. High-Level Text Language',
                                      'C. Hyper Transfer Markup Language'],
        'Which technology is used for styling web pages?': ['A. CSS', 'B. HTML', 'C. JavaScript'],
        'What is the purpose of JavaScript in web development?': [
            'A. To add interactivity and dynamic behavior to web pages',
            'B. To define the structure of web pages',
            'C. To style the appearance of web pages']
    }
}


def question_ans(question, choices):
    print(question)
    for option in choices:
        print(option)
    user_answer = input("Your answer:").upper()
    return user_answer


def run_quiz():
    score = 0

    print("Welcome to the Quiz Application!")

    for category, questions in quiz_questions.items():
        print(f"\n{category} Questions:\n")
        for question, options in questions.items():
            random.shuffle(options)
            user_answer = question_ans(question, options)

            correct_answer = [choice for choice in options if choice.startswith('A')][0]
            if user_answer == correct_answer[0]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}\n")

    print(f"\nYour final score is {score}/{len(quiz_questions)* len(questions) }")


if __name__ == "__main__":
    run_quiz()
