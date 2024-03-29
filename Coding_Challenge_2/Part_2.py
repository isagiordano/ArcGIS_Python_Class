# 2. List overlap
# Using these lists:
#
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

# Determine which items are present in both lists.
# transform lists into sets, intersect sets-
#what is a set? sets cannot have multiple occurrences of the same element and store unordered values.

set_a = set(list_a)
set_b = set(list_b)

# intersect set
intersected_set = set_a.intersection(set_b)
intersected_list = list(intersected_set)
print(intersected_list)

#!! referenced from https://favtutor.com/blogs/intersection-two-lists-python

# Determine which items do not overlap in the lists.
# make difference lists between sets

difference_list_b = [x for x in set_b if x not in set_a]
# make list for every variable x in set be that is not in set a
difference_list_a = [x for x in set_a if x not in set_b]
## make list for every variable x in set a that is not in set b
# combine lists
difference_list_a.extend(difference_list_b)
print(difference_list_a)

#!! referenced from https://www.geeksforgeeks.org/python-difference-two-lists/
