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
                line = f.readlines()
                print(line[0])
                ask_ans = input("enter your answer:").lower()
                with open("question.txt") as f:
                        answer = f.readlines()
                        real_ans = answer[1]
                        if ask_ans == real_ans:
                                print("correct answer")
                        
                        


        
        

    
    