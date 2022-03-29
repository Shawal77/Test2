from  tabulate import tabulate
coursesSemesterOne={
    'Engineering Maths 1':4,
    'Introduction to Electrical Engineering':3,
    'Physical Electronics':4,
    'Circuit Theory':4,
    'Communication Skills':2,
    'Information Computer technology':3}
total=sum(list(coursesSemesterOne.values()))
coursesSemesterOne['Total']=total
#we sum credit units
#print(tabulate(coursesSemesterOne.values()))
print(tabulate(
    list(coursesSemesterOne.items()),
    showindex='always',
    headers=['Course units','Credit units'],
    tablefmt='fancy_grid'
))
print('\n\nSemester One results')
for value in coursesSemesterOne:
    print(f'{value}  {coursesSemesterOne[value]}  {gradePointsSemesterOne[value]}  {letterGradeSemesterOne[value]}')
print(f'GRade point average: ',end='')
print('%.2f'%GPA1,end='. \n')
print('\nSemester two results')
for value in coursesSemesterTwo:
    print(f'{value}  {coursesSemesterTwo[value]}  {gradePointsSemesterTwo[value]}  {letterGradeSemesterTwo[value]}')
print(f'GRade point average: ',end='')
print('%.2f'%GPA2,end='. \n')
print(f'\n \nDear {studentFirstName} {studentSurname}, \nYou have a {degreeClassOverall}\nYour Cumulative grade point average is ',end='')
print('%.2f'%CGPA,end='. \n\n')