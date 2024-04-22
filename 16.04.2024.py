def add(x,y):
    return x+y
a = add(4,5)
print(a)


def append_to_list(x):
    list1 = [1,2,3,4]
    list1.append(x)
    return list1
print(append_to_list(5))

def add_to_list(x):
    list_1 = [
        {
            "name": "Kanat",
            "last_name": "Erbolov",
            "age": 20
        },
        {
            "name": "Askar",
            "last_name": "Erzhanov",
            "age": 15
        },
        {
            "name": "Kairat",
            "last_name": "Zhandosov",
            "age": 45
        }
]

    list_1.append(x)
    return list_1
print(add_to_list({"name":"Askar","lastname_name":"Dauletbay","age":16}))
