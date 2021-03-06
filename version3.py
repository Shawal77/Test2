from tabulate import tabulate
studentFirstName=input('Welcome to Electrical Engineering Year 2 CGPA calculator!\nWhat is your first name? ').capitalize()
studentSurname=input('What is your surname? ').capitalize()
# lets get courses in semester 1
coursesSemesterOne={'Engineering Maths 1':4,'Introduction to Electrical Engineering':3,'Physical Electronics':4,'Circuit Theory':4,'Communication Skills':2,'Information Computer technology':3}
coursesSemesterTwo={'EMT2':4,'EM':4,'Stat':2,'CMP':4,'DE':4,'Soc':3}
#we sum credit units
sumOfCreditUnitsSemesterOne=sum(list(coursesSemesterOne.values()))
sumOfCreditUnitsSemesterTwo=sum(list(coursesSemesterTwo.values()))
#we get grades points and pair then with the courses
gradePointsSemesterOne={}
letterGradeSemesterOne={}
percentMarksSemesterOne={}
for value in coursesSemesterOne:
    print(f'What is your mark in {value}? ',end=': ')
    studentMark=int(input())
    if studentMark<=100 and studentMark>=80:
        gradePoint=5
        letterGrade='A'
    elif studentMark>=70:
        gradePoint=4.5
        letterGrade='B+'
    elif studentMark>=60:
        gradePoint=4.0
        letterGrade='B'
    elif studentMark>=50:
        gradePoint=3.5
        letterGrade='C+'
    elif studentMark>=40:
        gradePoint=3.0
        letterGrade='C'
    elif studentMark>=30:
        gradePoint=2.5
        letterGrade='D+'
    elif studentMark>=20:
        gradePoint=2.0
        letterGrade='D'
    elif studentMark>=10:
        gradePoint=1.5
        letterGrade='E+'
    elif studentMark>=00:
        gradePoint=1.0
        letterGrade='E'
    gradePointsSemesterOne[value]= gradePoint
    letterGradeSemesterOne[value]= letterGrade
    percentMarksSemesterOne[value]=studentMark
#we get grades points and pair then with the courses
gradePointsSemesterTwo={}
letterGradeSemesterTwo={}
percentMarksSemesterTwo={}
for value in coursesSemesterTwo:
    print(f'What is your mark in {value}? ',end=' : ')
    studentMark=int(input())
    if studentMark<=100 and studentMark>=80:
        gradePoint=5
        letterGrade='A'
    elif studentMark>=70:
        gradePoint=4.5
        letterGrade='B+'
    elif studentMark>=60:
        gradePoint=4.0
        letterGrade='B'
    elif studentMark>=50:
        gradePoint=3.5
        letterGrade='C+'
    elif studentMark>=40:
        gradePoint=3.0
        letterGrade='C'
    elif studentMark>=30:
        gradePoint=2.5
        letterGrade='D+'
    elif studentMark>=20:
        gradePoint=2.0
        letterGrade='D'
    elif studentMark>=10:
        gradePoint=1.5
        letterGrade='E+'
    elif studentMark>=00:
        gradePoint=1.0
        letterGrade='E'
    gradePointsSemesterTwo[value]= gradePoint
    letterGradeSemesterTwo[value]= letterGrade
    percentMarksSemesterTwo[value]=studentMark
#we calculate the CGPA
def GPAGetter(coursesdictionary,gradePointsSemesterX,sumOfCreditUnits):
    weightedScores=[]
    for x in range(len(coursesdictionary)):
        weightedScore=(list(coursesdictionary.values())[x])*(list(gradePointsSemesterX.values())[x])
        weightedScores.append(weightedScore)
    totalWeightedScore=sum(weightedScores)
    CGPA=totalWeightedScore/sumOfCreditUnits
    return CGPA
GPA1=GPAGetter(coursesSemesterOne,gradePointsSemesterOne,sumOfCreditUnitsSemesterOne)
GPA2=GPAGetter(coursesSemesterTwo,gradePointsSemesterTwo,sumOfCreditUnitsSemesterTwo)
CGPA=(GPA1+GPA2)/2.0
#we get the degree type
def DegreeGetter(CGPA):
    if CGPA<=5 and CGPA>=4.4:degreeClass='First Class (Honours) Degree. Congragulations'
    elif CGPA>=3.6:degreeClass='Second Class-Upper Degree. Good work'
    elif CGPA>=2.8:degreeClass='Second Class-lower Degree. Aim higher'
    elif CGPA>=2.0:degreeClass='Pass. You have the potential to do better'
    else:degreeClass='Fail. '
    return degreeClass
degreeClassSemesterOne=DegreeGetter(GPA1)
degreeClassSemesterTwo=DegreeGetter(GPA2)
degreeClassOverall=DegreeGetter(CGPA)
#we print the output
#we want [course,gradepoint,letterGrade,]
print('\n\nSemester One results')
semOneResults=[]
for value in coursesSemesterOne:
    list1=[value,coursesSemesterOne[value],percentMarksSemesterOne[value],gradePointsSemesterOne[value],letterGradeSemesterOne[value]]
    semOneResults.append(list1)
print(tabulate(
    semOneResults,
    headers=['Course units','Credit units','Percentages','Grade Points','Letter'],
    tablefmt='fancy_grid'))
print(f'GRade point average: ',end='')
print('%.2f'%GPA1,end='. \n')
print('\nSemester two results')
semTwoResults=[]
for value in coursesSemesterTwo:
    list2=[value,coursesSemesterTwo[value],percentMarksSemesterTwo[value],gradePointsSemesterTwo[value],letterGradeSemesterTwo[value]]
    semTwoResults.append(list2)
print(tabulate(
    semTwoResults,
    headers=['Course units','Percentages','Credit units','Grade Points','Letter'],
    tablefmt='fancy_grid'))
print(f'GRade point average: ',end='')
print('%.2f'%GPA2,end='. \n')
print(f'\n \nDear {studentFirstName} {studentSurname}, \nYou have a {degreeClassOverall}\nYour Cumulative grade point average is ',end='')
print('%.2f'%CGPA,end='. \n\n')
