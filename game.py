import sys
print("Welcome to the Quiz Game !\n" )

print("1.enter the game")
print("2.exit")

user = int(input("enter your command: "))
if user == 2:
       sys.exit() 
else:
    name = input("enter your name: ")


      

with open("question.txt") as f:
                for line in f:
                    ques = line.readline().lower()
                print(ques)
                ask_ans = input("enter your answer:").lower()
                for answer in range(1):
                        ans_read = f.readline().lower()
                        
                        if ask_ans in ans_read:
                                print("correct answer")
                        else:
                            print(f"wrong,the correct answer was {ans_read}")
                            continue


        
        

    
    