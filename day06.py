from _collections import defaultdict

with open("data06.txt") as datafile:
    data = datafile.read().split()

data_tuples = [
    (orbit.split(")")[0], orbit.split(")")[1]) for orbit in data
]  # x[1] orbits x[0]
print(data_tuples)
orbits = defaultdict(list)
orbits_parents = dict()
for center, orbiter in data_tuples:
    orbits[center].append(orbiter)
    orbits_parents[orbiter] = center


def distance_from_root(orbits_parents_dict, node):
    current_node = node
    distance = 0
    while current_node != "COM":
        parent_node = orbits_parents_dict[current_node]
        current_node = parent_node
        distance += 1
    return distance


print(orbits_parents)
print(max([len(x) for x in orbits.values()]))

print(distance_from_root(orbits_parents, "COM"))

total_orbits = 0
for space_object in orbits_parents.keys():
    total_orbits += distance_from_root(orbits_parents, space_object)

print(total_orbits)
# 234446
