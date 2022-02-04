"""
© https://sudipghimire.com.np

Sets Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create two different set of countries
    i.  rich: {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
    ii. europe: {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}

    Use the Set methods to find out:

    a. countries that are rich but not in Europe
    b. countries that are in Europe but not rich
    c. countries that are both rich and are in Europe
    d. countries that are either rich or in Europe, but not both
    e. all the countries in either of the sets. (Names must be unique)
    f. see if two sets are disjoint or not
    g. now remove the common countries from the `rich` set and check if two sets are disjoint or not.
        - hint: use `difference_update()` method. for more, please refer to python documentation
"""

# answer 1.

# a
rich= {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
europe= {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}
rich.difference(rich.intersection(europe)) #or
rich-rich.intersection(europe)
# b
europe.difference(rich.intersection(europe)) #or
europe-rich.intersection(europe)

# c
rich.intersection(europe)

# d
rich.symmetric_difference(europe)
rich.union(europe).difference(rich.intersection(europe))
# e
rich.union(europe)

# f
rich.isdisjoint(europe)
# g


rich.difference_update(rich.intersection(europe))
europe.difference_update(rich.intersection(europe))
rich.isdisjoint(europe)
"""
2. Create two more sets
    i.  `asian_rich` and add {'China', 'Japan'} to it.
    ii. `american_rich` and add {'USA', 'Canada'} to it.
   and check whether:

   a. `asian_rich` is a subset of `rich` or not
   b. `rich` is a superset of `asian_rich` or not
   c. `american_rich` is a subset of `rich` or not

"""
# answer 2

# a
asian_rich={'China', 'Japan'}
american_rich={'USA', 'Canada'}
# b
asian_rich.issubset(rich)
rich.issuperset(asian_rich)

# c
american_rich.issubset(rich)