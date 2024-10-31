grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

my_dict = {}

students_list = list(students)

students_list.sort()

print(students_list)

average_grades = (sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
                  sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4]))

print(average_grades)

print({
    f'{students_list[0]}: {average_grades[0]}, {students_list[1]}: {average_grades[1]}, {students_list[2]}: {average_grades[2]}, '
    f'{students_list[3]}: {average_grades[3]}, {students_list[4]}: {average_grades[4]}'})
