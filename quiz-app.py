import random
import json

try:
    with open("last_score.json", "r") as file:
        last_score = json.load(file)
except FileNotFoundError:
    last_score = None

def save_score(score, total):
    with open("last_score.json", "w") as file:
        json.dump({"score": score, "total": total}, file)
def start_quiz():
     while True:
            random.shuffle(questions)
            score = 0
            for q in questions:
                print("\n" + q["question"])
                for option in q["options"]:
                    print(option)
                while True:
                    user_answer = input("Your answer (a/b/c/d): " + " ").strip().lower()
                    if user_answer in ["a", "b", "c", "d"]:
                        break
                    else:
                        print("Invalid choice, please enter a, b, c or d.")
                if user_answer == q["answer"]:
                    print ("Correct!")
                    score += 1
                else:
                    print("Wrong!")
                    for option in q["options"]:
                        if option.startswith(q["answer"]):
                            print("The correct answer is", option)

            print("Your final score is:", score, "/", len(questions) )
            again = input("Play again? (Yes/ No): ").strip().lower()
            if again == "no":
                save_score(score, len(questions))
                return{"score": score, "total": len(questions)}



def view_last_score(last_score):
    if last_score is None:
        print("No quiz played yet")
    else:
        print("Your last score is:", last_score["score"], "/", last_score["total"])


questions = [{
    "question": "What keyword is used to define a function in Python?",
    "options": ["a) func","b) def", "c) function", "d) define"],
    "answer": "b"
},
{
    "question": "What loop is used when you want to repeat while a condition is true?",
    "options": ["a) while","b) for", "c) repeat", "d) loop"],
    "answer": "a"
},
{
    "question": "What function gives the length of a list?",
    "options": ["a) size","b) count", "c) length", "d) len"],
    "answer": "d"
}]
score = None
while True:
    print("\n1-Start quiz")
    print("2-View last Score")
    print("3-Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        last_score = start_quiz()
            
    elif choice == "2":
        view_last_score(last_score)

    elif choice == "3":
        break
    else:
        print("Invalid Choice")
    

