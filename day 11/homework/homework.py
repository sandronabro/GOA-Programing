# დავ 1
x = [2, 4, 6, 2, 4, 7, 2, 9]

while 4 in x:
    x.remove(4)
print(x)

# დავ 2
# ვარიანტი 1

family = ["tea","saba","sandro"]
age = [42, 18, 13]
full_sentence = "My moms name is: {} Her age is: {}, My brothers name is: {} His age is: {}, My name is: {} My age is: {}, In 10 years, my mom will be {}, My brother will be {}, and i will be {} years old.".format(family[0],age[0],family[1],age[1],family[2],age[2],age[0] + 10, age[1] + 10, age[2] + 10)
print(full_sentence)

# ვარიანტი 2

family = ["tea","saba","sandro"]
age = [42, 18, 13]
full_sentence = "My moms name is: {} Her age is: {}, My brothers name is: {} His age is: {}, My name is: {} My age is: {}".format(family[0],age[0],family[1],age[1],family[2],age[2])
print(full_sentence)
future_age = "In 10 years, my mom will be {}, My brother will be {}, and i will be {} years old.".format(age[0] + 10, age[1] + 10, age[2] + 10)
print(future_age)