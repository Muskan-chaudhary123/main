# serialisation : covert list into JSON format and then read
"""import json
l = [1,2,3,4,5]
with open("demo.json", 'w') as f:
    json.dump(l, f,indent=4)"""

# Deserialization :
"""import json
with open("demo.json", "r") as f:
    print(json.load(f))"""

# serialization and deserialization with tuple
"""import json
t = (1,2,3,4,5)
with open("demo.json", 'r') as f:
    d = json.load(f)
    print(tuple(d))
    print(type(d))"""

"""import json
d = {
    'name': 'rohan',
    'class': 'cse1',
    'marks': {
        'phys': 89,
        'maths': 98,
        'chemistry': 99
    },
    'rank': 5
}
with open("demo.json", 'r') as f:
    s = json.load(f)
    print(s)"""


"""class Person:
    def __init__(self, f_name, l_name, age, gender):
        self._name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender


person = Person("rohan", "chaudhary", 33, 'female')

import json


def show_obj(person):
    if isinstance(person, Person):
        return "{} {} age -> {} gender -> {}".format(person.f_name, person.l_name, person.age, person.gender)


with open("demo.json", 'w') as f:
    json.dump(person, f, default=show_obj)
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("hi my name is ",self.name,"and i am ",self.age,"years old")


p = Person("rohan",33)

import pickle
with open('person.pkl', 'rb') as f:
     q = pickle.load(f)
q.display_info()
































