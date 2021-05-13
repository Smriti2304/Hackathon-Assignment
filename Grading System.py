def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            if grade % 5 == 0:
                rounded_grades.append(grade)
            else:
                difference = 0
                new_grade = grade
                while grade % 5 != 0:
                    difference += 1
                    new_grade += 1
                    if new_grade % 5 == 0:
                        break
                if difference < 3:
                    rounded_grades.append(new_grade)
                else:
                    rounded_grades.append(grade)
    return rounded_grades


