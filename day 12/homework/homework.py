def triangles(a,b,c):
    
    if a + b > c and a + c > b and b + c > a:
        print("ასეთი სამკუთხედი იარსებებს")
    else:
        print("ასეთი სამკუთხედი ვერ იარსებებს")

triangles(3,7,9)
triangles(4,1,2)
triangles(9,3,4)

def saxeli(name1,name2,name3):

    names = ",".join([name1,name2,name3])
    names_split = names.split(' ')
    print(names_split)

saxeli('sandro','saba','koba')