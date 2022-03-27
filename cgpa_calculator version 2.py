from tabulate import tabulate
studentFirstName=input('Welcome to Electrical Engineering Year 2 CGPA calculator!\nWhat is your first name? ').capitalize()
studentSurname=input('What is your surname? ').capitalize()

# lets get courses in semester 1
coursesSemesterOne={
    'Engineering Maths 1':4,
    'Introduction to Electrical Engineering':3,
    'Physical Electronics':4,
    'Circuit Theory':4,
    'Communication Skills':2,
    'Information Computer technology':3}
#we sum credit units
sumOfCreditUnits=sum(list(coursesSemesterOne.values()))

#we get grades points and pair then with the courses
gradePointsSemesterOne={}
for value in coursesSemesterOne:
    print(f'What is your mark in {value}? ',end=' : ')
    studentMark=int(input())
    if studentMark<=100 and studentMark>=80:gradePoint=5
    elif studentMark>=70:gradePoint=4.5
    elif studentMark>=60:gradePoint=4.0
    elif studentMark>=50:gradePoint=3.5
    elif studentMark>=40:gradePoint=3.0
    elif studentMark>=30:gradePoint=2.5
    elif studentMark>=20:gradePoint=2.0
    elif studentMark>=10:gradePoint=1.5
    elif studentMark>=00:gradePoint=1.0
    gradePointsSemesterOne[value]= gradePoint
#we calculate the CGPA
def GPAGetter(dictionary,gradePointsSemesterX):
    weightedScores=[]
    for x in range(len(dictionary)):
        weightedScore=list(coursesSemesterOne.values())[x]*list(gradePointsSemesterX.values())[x]
        weightedScores.append(weightedScore)
    totalWeightedScore=sum(weightedScores)
    CGPA=totalWeightedScore/sumOfCreditUnits
    return CGPA
#we get the degree type
CGPA=GPAGetter(coursesSemesterOne,gradePointsSemesterOne)
if CGPA<=5 and CGPA>=4.4:degreeClass='First Class (Honours) Degree. Congragulations'
elif CGPA>=3.6:degreeClass='Second Class-Upper Degree. Good work'
elif CGPA>=2.8:degreeClass='Second Class-lower Degree. Aim higher'
elif CGPA>=2.0:degreeClass='Pass. You have the potential to do better'
else:degreeClass='Fail. '
#we print the output
gradePointsSemesterOne['CGPA']=CGPA
print(tabulate(
    list(gradePointsSemesterOne.items()),
    showindex='always',
    headers=['Course units','Grade points'],
    tablefmt='fancy_grid'
))
print(f'Dear {studentFirstName} {studentSurname}, you have a {degreeClass}\nYour Cumulative grade point average is ',end='')
print('%.2f'%CGPA,end='. \n')