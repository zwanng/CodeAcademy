#import random function, and set up variables
import random
name = "James"
question = "Will I win in the lottery?"
answer = ""

#check if the name is empty or not. Empty name will just output question
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: "+question)

#if-else structure, if the question is empty, print a message to users, otherwise 
#continue Magic 8-Ball
if question == "":
  print("No question, the Magic 8-Ball can not provide a fortune")
else:
  random_number = random.randint(1,9)
  if(random_number == 1):
    answer = "Yes-definitely"
  elif(random_number == 2):
    answer = "It is decidedly so"
  elif(random_number == 3):
    answer = "Without a doubt"
  elif(random_number == 4):
    answer = "Reply hazy, try again"
  elif(random_number == 5):
    answer = "Ask again later"
  elif(random_number == 6):
    answer = "Better not tell you now"
  elif(random_number == 7):
    answer = "My sources say no"
  elif(random_number == 8):
    answer = "Outlook not so good"
  elif(random_number == 9):
    answer = "Very doubtful"
  else:
    answer = "Error"
  print("Magic 8-Ball's answer: "+answer)
