dict1={'Engineering Maths 1':4,'Introduction to Electrical Engineering':3,'Physical Electronics':4,'Circuit Theory':4,'Communication Skills':2,'Information Computer technology':3}
dict2={'Engineering Maths 1':4,'Introduction to Electrical Engineering':3,'Physical Electronics':4,'Circuit Theory':4,'Communication Skills':2,'Information Computer technology':3}
def merge(dict1,dict2):
    dict3={**dict1,**dict2}
    for key in dict1 and key in dict2:
        dict3[key]=[value,dict1[key]]
    return dict3
final = merge(dict1,dict2)
print(final)