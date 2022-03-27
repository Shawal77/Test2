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