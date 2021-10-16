# Wefqi Odeh
# This is my example of Matchmaker Assignment

print ("")
print("Wefqi Odeh Matchmaker 2021")
print ("")
print("Hello! Welcome to Wefqi's Version of Matchmaker. This this questionair you will be asked a series of quesiton and you must answer truthfully with the numbers 1-5. 1-  Strongly Disagree, 2-Disagree, 3-so and so, 4- Agree, and 5- Totaly Agree! Lets Begin, but first what is your name?")
print("")

Answer0 = (input("What is Your Name?"))
print ("Hello!" + str(Answer0))

Answer1=int(input("I Hate Onions"))
CorrectAnswer1=5
Calculation1= 5 - abs(Answer1- CorrectAnswer1)
print("Question 1 Results " + str(Calculation1))
print("")

Answer2=int(input("I Love Binging Netflix"))
CorrectAnswer2=5
Calculation2= 5 - abs(Answer2- CorrectAnswer2)
print("Question 2 Results " + str(Calculation2))
print("")

Answer3=int(input("I Dont Like Videogames"))
CorrectAnswer3=1
Calculation3= 5 - abs(Answer3- CorrectAnswer3)
print("Question 3 Results " + str(Calculation3))
print("")

Answer4=int(input("I love the Winter"))
CorrectAnswer4=5
Calculation4= 5 - abs(Answer4- CorrectAnswer4)
print("Question 4 Results " + str(Calculation4))
print("")

Answer5=int(input("I love Sand"))
CorrectAnswer5=1
Calculation5= 5 - abs(Answer5- CorrectAnswer5)
print("Question 5 Results " + str(Calculation5))
print("")

OverallScore = (Calculation1 + Calculation2 + Calculation3 + Calculation4 + Calculation5) * 4
print ("OverallScore: " + str(OverallScore))
print("")