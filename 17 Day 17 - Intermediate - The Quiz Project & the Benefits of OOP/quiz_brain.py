class QuizBrain:
    def __init__(self, q_list):
        self.question_Number = 0
        self.question_List = q_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_Number < len(self.question_List)    
        # if self.question_Number < len(self.question_List):
        #     return True
        # else:
        #     return False


    def next_Question(self):
        currentQuestion = self.question_List[self.question_Number]
        self.question_Number += 1
        userAnswer = input(f"Q.{self.question_Number}: {currentQuestion.text} (True / False): ")
        self.checkAnswer(userAnswer, currentQuestion.answer)
        
    def checkAnswer(self, userAnswer, correct_Answer):
        if userAnswer.lower() == correct_Answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_Answer}")
        print(f"Your current score is {self.score} / {self.question_Number}")
        print("\n")