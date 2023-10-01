# colors = ['red', 'blue']
# colors.append('black')
# print(colors)
# colors.extend(['babyblue', 'neonpink'])
# print(colors)
# colors.pop(2)
# print(colors)
# colors.remove('neonpink')
# print(colors)
# colors.reverse()
# print(colors)
grade = [65, 78, 101, 88, 55, 78]

#sort the list from smallest to largest
grade.sort()
print(grade)

# insert object at an given index, moving items to make room
grade.insert(3, 202)
print(grade)

print(grade.count(78))
print(grade.index(101))


