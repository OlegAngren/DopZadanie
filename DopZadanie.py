
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в отсортированный список, чтобы порядок соответствовал списку оценок
students_list = sorted(students)

# Находим индекс ученика 'Aaron'
index_aaron = students_list.index('Aaron')

# Рассчитываем средний балл для 'Aaron'
average_grade_aaron = sum(grades[index_aaron]) / len(grades[index_aaron])

# Находим индекс ученика 'Bilbo'
index_bilbo = students_list.index('Bilbo')

# Рассчитываем средний балл для 'Bilbo'
average_grade_bilbo = sum(grades[index_bilbo]) / len(grades[index_bilbo])


# Находим индекс ученика 'Johnny'
index_johnny = students_list.index('Johnny')

# Рассчитываем средний балл для 'Johnny'
average_grade_johnny = sum(grades[index_johnny]) / len(grades[index_johnny])

# Находим индекс ученика 'Khendrik'
index_khendrik = students_list.index('Khendrik')

# Рассчитываем средний балл для 'Khendrik'
average_grade_khendrik = sum(grades[index_khendrik]) / len(grades[index_khendrik])

# Находим индекс ученика 'Steve'
index_steve = students_list.index('Steve')

# Рассчитываем средний балл для 'Steve'
average_grade_steve = sum(grades[index_steve]) / len(grades[index_steve])

average_grades = {'Aaron':average_grade_aaron,'Bilbo': average_grade_bilbo ,'Johnny': average_grade_johnny,'Khendrik': average_grade_khendrik,'Steve':average_grade_steve}

print(average_grades)



