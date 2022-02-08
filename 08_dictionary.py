"""
© https://sudipghimire.com.np

Dictionary Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Create a dictionary of a person that contains key value pair of
    - name: str
    - age: int
    - profession: str
    - married: bool

    a. print the value of 'name' from the dictionary
    b. add the age of the dictionary be 10 and print the dictionary items in formatted string
        Eg: {name} will be {new_age} at 2031 AD.
    c. Try getting the value of 'employed' from the dictionary.
        - If exception occurs, note it and check what the excption says.
    d. try `get()` method instead of large brackets [] in the previous question (1.c)
    e. try `get()` method with second parameter: False and see what is printed.
        Eg: person.get('employed', False)
"""
# Answers:

# 1.a
from os import remove


human = {
    'name': 'jimmy',
    'age': 24,
    'profession':'professor',
    'married': False,
    }
print(human['name'])

# 1.b
new_age =human['age']+10

human.update({'age': new_age})

print(f"In 2031 {human['name']} will be {human['age']} years old. ")

# 1.c

print(human['employed'])
# 1.d
x=human.get('employed')

print(x)

# 1.e
x=human.get('employed',False)

print(x)

"""
2. create a dictionary <car> with 3 keys and values (brand, model, price).
    a. add a new key 'engine' and set some random value in car.
    b. add 3 more dictionary keys with `update` method. (color, no_of_seats, transmission).
    c. remove the key 'color' from the dictionary.
    d. try using `popitem()` method in the dictionary and see what changes in dictionary
    e. use for loop to iterate through all keys from a dictionary.
    f. use for loop to iterate through all keys from a dictionary using `keys()` method.
    g. use for loop to iterate through all values from a dictionary using `values()` method.
    h. use for loop to iterate through all keys, values from a dictionary using `items()` method.
"""
# Answers:

# 2.a
car={'brand':'toyota','model':'camry','price':28000}
car={**car,'engine':'V6'}

# 2.b
car.update({'color':'red',' no_of_seats':5, 'transmission':'Automatic'})

# 2.c
del car['color']
# 2.d
item=car.popitem()
item[0]
item[1]

# 2.e
for key in car:
    print(key)
    print(car[key])

# 2.f

for x in car.keys():
    print(x)

# 2.g
for x in car.values():
    print(x)

# 2.h
for item in car.items():
    print(item)

"""
3. Create a nested dictionary named yoda with following properties
    - age: 910
    - species: Yodas
    - gender: male
    - affilitions: ['Jedi', 'Galactic Republic']
    - master: {
        - name: Qui-Gon Jinn
        - age: 48
        - affiliations: ['Jedi', 'Galactic Republic', 'Heliost Clan']},
        - master: {
            - name: Dooku
            - age: 83
            - affiliations: ['House Serenno', 'Jedi']}

    a. print the value of the first affiliation of `Dooku` from the dictionary
    b. add new affiliation 'Sith' to Dooku
    c. pop the key 'master' from the dictionary

"""
# Answer 3
yoda={
     'age': 910,
     'species': 'Yodas',
     'gender': 'male',
     'affilitions': ['Jedi', 'Galactic Republic'],
     'master': {
        'name': 'Qui-Gon Jinn',
        'age': 48,
        'affiliations': ['Jedi', 'Galactic Republic', 'Heliost Clan'],
            'master':{
              'name': 'Dooku',
              'age': 83,
              'affiliations': ['House Serenno', 'Jedi']}
                }
      }
# 3.a
print(yoda["master"]["master"]["affiliations"][0])

# 3.b
yoda["master"]["master"]["affiliations"]=['House Serenno', 'Jedi','seth']

# 3.c
yoda.popitem()



