from tabulate import tabulate
studentFirstName=input('Welcome to Electrical Engineering Year 2 CGPA calculator!\nWhat is your first name? ').capitalize()
studentSurname=input('What is your surname? ').capitalize()
# lets get courses in semester 1
coursesSemesterOne=['Engineering Maths 1','Introduction to Electrical Engineering','Physical Electronics','Circuit Theory','Communication Skills','Information Computer technology']
creditUnitsSemesterOne=[4,3,4,4,2,3]
coursesSemesterTwo=['EMT2','EM','Stat','CMP','DE','Soc']
creditUnitsSemesterTwo=[4,4,2,4,4,3]
#we sum credit units
sumOfCreditUnitsSemesterOne=sum(creditUnitsSemesterOne)
sumOfCreditUnitsSemesterTwo=sum(creditUnitsSemesterTwo)
#we get grades points and pair then with the courses
gradePointsSemesterOne=[]
letterGradeSemesterOne=[]
percentMarksSemesterOne=[]
for x in range(len(coursesSemesterOne)):
    print(f'What is your mark in {coursesSemesterOne[x]}? ',end=': ')
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
    gradePointsSemesterOne.append(gradePoint)
    letterGradeSemesterOne.append(letterGrade)
    percentMarksSemesterOne.append(studentMark)
#we get grades points and pair then with the courses
gradePointsSemesterTwo=[]
letterGradeSemesterTwo=[]
percentMarksSemesterTwo=[]
for x in range(len(coursesSemesterTwo)):
    print(f'What is your mark in {coursesSemesterOne[x]}? ',end=' : ')
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
    gradePointsSemesterTwo.append(gradePoint)
    letterGradeSemesterTwo.append(letterGrade)
    percentMarksSemesterTwo.append(studentMark)
#we calculate the CGPA
def GPAGetter(creditUnitsSemesterX,gradePointsSemesterX,sumOfCreditUnits):
    weightedScores=[]
    for x in range(len(creditUnitsSemesterX)):
        weightedScore=(creditUnitsSemesterX[x])*(gradePointsSemesterX[x])
        weightedScores.append(weightedScore)
    totalWeightedScore=sum(weightedScores)
    CGPA=totalWeightedScore/sumOfCreditUnits
    return CGPA
GPA1=GPAGetter(creditUnitsSemesterOne,gradePointsSemesterOne,sumOfCreditUnitsSemesterOne)
GPA2=GPAGetter(creditUnitsSemesterTwo,gradePointsSemesterTwo,sumOfCreditUnitsSemesterTwo)
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
#we print the output semester1
print('\n\nSemester One results'.upper())
print('{}'.format('#'*(39+11+12+13+13+3)))
print("{:39}{:11}{:12}{:13}{:14}|".format('|Course','|Credit Unit','|Percentage','|Grade point','|Letter Grade'))#table headers
print('{}'.format('#'*(39+11+12+13+13+3)))
for x in range(len(coursesSemesterOne)):
    #provided longest course nAME is 38 characters
    print(f'|{coursesSemesterOne[x]:38}|{creditUnitsSemesterOne[x]:11d}|{percentMarksSemesterOne[x]:11d}|{gradePointsSemesterOne[x]:12f}|{letterGradeSemesterOne[x]:>13}|')
print('{}'.format('#'*(39+11+12+13+13+3)))
print(f'GRade point average: ',end='')
print('%.2f'%GPA1,end='. \n')
#we print the output semester1
print('\nSemester two results'.upper())
print('{}'.format('#'*(39+11+12+13+13+3)))
print("{:39}{:11}{:12}{:13}{:14}|".format('|Course','|Credit Unit','|Percentage','|Grade point','|Letter Grade'))#table headers
print('{}'.format('#'*(39+11+12+13+13+3)))
for x in range(len(coursesSemesterTwo)):
    #provided longest course nAME is 38 characters
    print(f'|{coursesSemesterTwo[x]:38}|{creditUnitsSemesterTwo[x]:11d}|{percentMarksSemesterTwo[x]:11d}|{gradePointsSemesterTwo[x]:12f}|{letterGradeSemesterTwo[x]:>13}|')
print('{}'.format('#'*(39+11+12+13+13+3)))
print(f'GRade point average: ',end='')
print('%.2f'%GPA2,end='. \n')
#we print the conclusion statement
print(f'\n \nDear {studentFirstName} {studentSurname}, \nYou have a {degreeClassOverall}\nYour Cumulative grade point average is ',end='')
print('%.2f'%CGPA,end='. \n\n')
