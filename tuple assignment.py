"""
© https://sudipghimire.com.np

Tuple Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create a tuple to  add 5 different numbers.
    a. find out the length of the tuple
    b. find out the 3rd element of the tuple by accessing it through the index
    c. use `enumerate()` function to map each element with its index and print it using the foreach loop
        - please see the reference to the file 02_data_types/06_tuples.py

"""
# answer 1


# a
from operator import index


Numbs=(76,57,63,79,44)
print(sum(Numbs))
print(len(Numbs))

# b
print(Numbs[2])

# c
for items in enumerate(Numbs):
    print(f'[index]=[{items}]')

"""
2. Write a program to create a nested tuple and access different elements of the inner tuple using
   positive and negative index positions.

"""
Numbs1=(76,57,63,79,44,(45,78,33),(87,92,35),49,88)
print(Numbs1[1])
print(Numbs1[-3][-2])

"""
Bonus:
3. create two different tuples t1 and t2 with different elements inside it
    a. create the next tuple t3 to add all values of t1 and t2 using the destructuring method

    - suppose t1 has (1,6,9,4,3)
    - and t2 has (2,7,8,3,5)
    -t3 must have (1,6,9,4,3,2,7,8,3,5)
    - make sure to use destructuring method using `*` operator in the tuples
"""
t1=(1,6,9,4,3)
t2=(2,7,8,3,5)
t3=(*t1,*t2)
print(t3)