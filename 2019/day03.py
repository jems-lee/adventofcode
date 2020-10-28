from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Point(
            self.x - other.x,
            self.y - other.y
        )

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def manhatten_distance(self, other):
        new = self - other
        return abs(new.x) + abs(new.y)


def read_file_as_string(file_name="data03.txt"):
    with open(file_name) as datafile:
        data = datafile.read()
    return data


def split_string_into_list_of_tuples(one_wire_string):
    wire = [(x[0], int(x[1:])) for x in one_wire_string.split(',')]
    return wire


def create_grid(m, n):
    grid = [
        [[0, 0] for i in range(n)] for j in range(m)
    ]
    return grid


def expand_path(path_tuples, grid, path_num=0):
    m = len(grid)
    n = len(grid[1])
    intersections = []
    path = list()
    path.append(Point(0, 0))
    step = 0
    for (direction, magnitude) in path_tuples:
        for i in range(magnitude):
            previous_point = path[-1]
            if direction == "R":
                point_change = Point(x=1, y=0)
            elif direction == "U":
                point_change = Point(x=0, y=1)
            elif direction == "L":
                point_change = Point(x=-1, y=0)
            elif direction == "D":
                point_change = Point(x=0, y=-1)
            else:
                raise IndexError(f"Not R, U, L, or D, it was {direction}")
            new_point = previous_point + point_change
            grid_point = grid[m // 2 + new_point.y][n // 2 + new_point.x]
            step += 1
            grid_point[path_num] = step
            if grid_point[0] != 0 and grid_point[1] != 0:
                # print(f"grid point: {grid_point}")
                intersections.append(Point(grid_point[0], grid_point[1]))
            path.append(new_point)
    return grid, intersections


def main():
    data = read_file_as_string("data03.txt")
    both_wires = data.split()
    wire1 = split_string_into_list_of_tuples(both_wires[0])
    wire2 = split_string_into_list_of_tuples(both_wires[1])
    grid = create_grid(10000, 10000)
    grid, intersections = expand_path(wire1, grid, path_num=0)
    print(f"intersections after 1: {intersections}")
    grid, intersections = expand_path(wire2, grid, path_num=1)
    print(f"intersections after 2: {intersections}")
    print(min([point.manhatten_distance(Point(0, 0)) for point in intersections]))

    # grid, intersections = expand_path_on_grid(grid, path1)
    # print(intersections)
    # grid, intersections = expand_path_on_grid(grid, path2)
    # print(intersections)
    # intersections = find_intersections(path1, path2)
    # print(intersections)


if __name__ == "__main__":
    main()
