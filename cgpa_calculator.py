#we get students names
studentFirstName=input('What is your first name? ').capitalize()
studentSurname=input('What is your surname? ').capitalize()

#we get grades as letters which we convert to grade points
userInput=input('What are your letter grades with spaces between the letters? ')
def interpret(command: str):
        return command.replace("A","5").replace("B","4").replace("C","3").replace("D","2").replace("E","1").replace("F","0").replace("a","5").replace("b","4").replace("c","3").replace("d","2").replace("e","1").replace("f","0")
gradePointString=interpret(userInput)
gradePoints=list(map(int,(gradePointString.split())))
#gradePoints=list(map(int,(input('Enter your grade points: ').split())))
#before this was getting GPs as numbers
#we have a better method line 6 to get it from letters
coursesSemesterOne={
    'Engineering Maths 1':4,
    'Introduction to Electrical Engineering':3,
    'Physical Electronics':4,
    'Circuit Theory':4,
    'Communication Skills':2,
    'Information Computer technology':3
    }
sumOfCreditUnits=sum(coursesSemesterOne)
#we calculate the CGPA
def GPAGetter():
    weightedScores=[]
    for key in range(len(coursesSemesterOne)):
        weightedScore=coursesSemesterOne[x]*gradePoints[x]
        weightedScores.append(weightedScore)
    totalWeightedScore=sum(weightedScores)
    CGPA=totalWeightedScore/sumOfCreditUnits
    #we get the degree type
    if CGPA<=5 and CGPA>=4.4:
        degreeClass='First Class (Honours) Degree. Congragulations'
    elif CGPA>=3.6:
        degreeClass='Second Class-Upper Degree. Good work'
    elif CGPA>=2.8:
        degreeClass='Second Class-lower Degree. Aim higher'
    elif CGPA>=2.0:
        degreeClass='Pass. You have the potential to do better'
    else:
        degreeClass='Fail. '
    #we print the output
    print(f'Dear {studentFirstName} {studentSurname}, you have a {degreeClass}\nYour Cumulative grade point average is ',end='')
    print('%.2f'%CGPA,end='. \n')
#we call our method to effect the defined function

print(f'Hello {studentFirstName}, welcome to second year CGPA calculator')
GPAGetter()
#we get list of first dem courses
#we get list of first dem courses CUs
#GRading
#User input final mark
#get a mark for each subjet 
