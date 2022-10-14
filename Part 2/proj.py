import mysql.connector
import sys

#connects to the sql database
mydb = mysql.connector.connect(
host="localhost",
user="dbuser",
password="Iwilldowell",
database="cs482502"
)

#Takes qeustion number to be solved as a parameter and calls appropriate function to solve the question
def main(num, ques):
    if(num == '1'):
        if (ques == ""):
            print("A further parameter is needed for this question")
        else:
            question1(ques)
    elif(num == '2'):
        if (ques == ""):
            print("A further parameter is needed for this question")
        else:
            question2(ques)
    elif(num == '3'):
        if (ques != ""):
            print("No further parameter needed for this question")
        else:
            question3()
    elif(num == '4'):
        if (ques == ""):
            print("A further parameter is needed for this question")
        else:
            question4(ques)
    elif(num == '5'):
        if (ques != ""):
            print("No further parameter needed for this question")
        else:
            question5()
    elif(num == '6'):
        if (ques == ""):
            print("A further parameter is needed for this question")
        else:
            question6(ques)
    elif(num == '7'):
        if (ques != ""):
            print("No further parameter needed for this question")
        else:
            question7()
    elif(num == '8'):
        if (ques != ""):
            print("No further parameter needed for this question")
        else:
            question8()
    else:
        print("Invalid question number provided, must be 1-8")


#solves question 1
def question1(streetName):
    mycursor = mydb.cursor()
    query="SELECT * FROM SITE WHERE ADDRESS LIKE '%"+streetName+"%'"
    mycursor.execute(query)

    for x in mycursor:
        print(x)


#solves question 2
def question2(SchedSystem):
    mycursor = mydb.cursor()
    query="SELECT * FROM DIGITALDISPLAY WHERE SCHEDULERSYSTEM='"+SchedSystem+"'"
    mycursor.execute(query)

    for x in mycursor:
        print(x)


#solves question 3
def question3():
    print('3')


#solves question 4
def question4(PhoneNo):
    print('4')


#solves question 5
def question5():
    print('5')


#solves question 6
def question6(ModelNo):
    print('6')


#solves question 7
def question7():
    print('7')


#solves question 8
def question8():
    print('8')



#pulls arguments and calls main
questionNumber = str(sys.argv[1])
questionParam = ""

#pulls second argument after question number
if (len(sys.argv) > 2):
    for i in range(len(sys.argv)):
        if i > 1:
            if (i != len(sys.argv)-1):
                questionParam+=sys.argv[i]+" "
            else:
                questionParam+=sys.argv[i]
    
main(questionNumber, questionParam)