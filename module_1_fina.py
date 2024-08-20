grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

aaron = sum(grades[0])/len(grades[0])
bilbo = sum(grades[1])/len(grades[1])
johnny = sum(grades[2])/len(grades[2])
khendrik = sum(grades[3])/len(grades[3])
steve = round(sum(grades[4])/len(grades[4]))

students_with_grade = {'Aaron': aaron,
                       'Bilbo': bilbo,
                       'Johnny': johnny,
                       'Khendrik': khendrik,
                       'Steve': steve}

print(students_with_grade)