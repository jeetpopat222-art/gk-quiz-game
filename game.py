import sys
name = input("enter your name: ")
print(f"Welcome to the Quiz Game {name}!\n" )


right_answer = 0
wrong_answer = 0

print("1.enter the game")
print("2.exit")

user = int(input("enter your command: "))
if user == 2:
       sys.exit() 
else:
      with open("question.txt") as f:
        ques = f.readlines()
        for i in range(0,40,2):
                        question = ques[i].strip().lower()
                        print(question)
                        ask_ans = input("enter your answer: ").lower()
                        if ask_ans == "ttt":
                                break

                        answer = ques[i+1].strip().lower()
                        if ask_ans == answer:
                                        right_answer += 1
                        elif ask_ans != answer:
                                        wrong_answer += 1
                                       


print(right_answer)
print(wrong_answer)

print("thanks for playing the game(:")                        

        
        

    
    