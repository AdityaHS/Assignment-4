#Question-3
#multiplication_game_for_kids
import random
for i in range(9):
   a=random.randint(1,100)
   b=random.randint(1,100)  
   print('question',i+1,':',a,'x',b,'=')
   result=a*b
   correct=0
   Q=int(input('enter your answer:'))
   if(Q==result):
      print('Right!')
   else:
      print('Wrong.Answer is',result)    