setA={1,2,3,4,5,6,6}
print(setA)
setB={5,6,7,8,9,10}
set_union=setA.union(setB)
print("union of set A and B:",set_union)
set_intersection=setA.intersection(setB)
print("intersection of set A and B:",set_intersection)
set_difference=setA.difference(setB)
print("difference of set A and B:",set_difference)
set_difference=setB.difference(setA)
print("difference of set B and A:",set_difference)