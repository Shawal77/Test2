#Here we will write the test data for the CGPA calcul
userInput=input('What are your letter grades? ')
def interpret(command: str):
        return command.replace("A","5").replace("B","4").replace("C","3").replace("D","2").replace("E","1").replace("F","0").replace("a","5").replace("b","4").replace("c","3").replace("d","2").replace("e","1").replace("f","0")
gradePointString=interpret(userInput)
gradePoints=list(map(int,(gradePointString.split())))