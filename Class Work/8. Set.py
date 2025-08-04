#A set is an unordered, mutable collection of unique elements.
#Set Creation
myset={1,2,3,2,42,3,4}
print(myset)#{1, 2, 3, 4, 42}
# Creating an empty set (use set() function, not {})
empty_set = set()

#Membership Testing
new_set={1,2,3,4,2,1}
print(1 in new_set)#True
print(6 in new_set)#False

#a. Union (| or union() method)->returns common elements
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2
print(result) # Output: {1, 2, 3, 4, 5}

#b. Intersection (& or intersection() method)
result2=set1 & set2
print(result2)#output:{3}

#c. Difference (- or difference() method)
result3=set1-set2
print(result3)#output:{1, 2}

#d. Symmetric Difference (^ or symmetric_difference() method)-Returns elements in either set1 or set2 but not both.
result4 = set1 ^ set2
print(result4)
# Output: {1, 2, 4, 5}

#e. Subset (<= or issubset() method)
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1 <= set2) # Output: True

#f. Superset (>= or issuperset() method)
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1 >= set2) # Output: True

#g. Disjoint Sets (isdisjoint() method)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # Output: True