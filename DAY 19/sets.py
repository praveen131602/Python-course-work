s1 = set(map(int,input("Enter elements of set 1: ").split()))
s2 = set(map(int,input("Enter elements of set 2: ").split()))

print(f'Union: {s1|s2}')
print(f'Intersection:{s1&s2}')
print(f'Difference(Set1-Set2):{s1-s2}')

