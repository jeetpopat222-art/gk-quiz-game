with open("question.txt") as f:
                       for ques in range(2):
                              read = f.readline().lower()
                              print(read)
                              ask_ans = input("enter your answer:").lower()
                              for answer in range(2):
                                     ans_read = f.readline().lower()

                                     if ask_ans in ans_read:
                                            print("correct answer")
                                     else:
                                            print(f"wrong,the correct answer was{ans_read}")
                                            continue
        
        
        
