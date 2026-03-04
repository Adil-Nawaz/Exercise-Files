'''

#creating or defining a class
class User:
#constructor #this constuctor will run and initialize attributes of class object whenever the object is created
#Attributes
    def __init__(self, user_Id, username):
        self.id = user_Id
        self.username = username
        self.followers = 0
        self.following = 0
#Methods
    def follow(self, user):
        user.followers =+ 1
        self.following += 1

#creating object from class
user_1 = User(101, "Adil")
user_2 = User(102, "Nawaz")
user_1.follow(user_2)
print(f"UserID: {user_1.id}\nUsername: {user_1.username}\nFollowers: {user_1.followers}\nFollowing: {user_1.following}")
print(f"UserID: {user_2.id}\nUsername: {user_2.username}\nFollowers: {user_2.followers}\nFollowing: {user_2.following}")

'''
#Quiz App Project
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [
]
for questions in question_data:
    question_text = questions["text"]
    question_anser = questions["answer"]
    newQuestion = Question(question_text, question_anser)
    question_bank.append(newQuestion)

newQuiz  = QuizBrain(question_bank)
while newQuiz.still_has_questions():
    newQuiz.next_Question()

print(f"You have completed the quiz and your final score is {newQuiz.score} / {len(question_bank)}")

