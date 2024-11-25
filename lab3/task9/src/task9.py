import math
from lab3.utils import read_from_file, write_in_file, quicksort_with_key


def distance(first_point, second_point):
    return math.sqrt((first_point[0] - second_point[0]) ** 2 +
                     (first_point[1] - second_point[1]) ** 2)


def closest_pair_in_strip(points, delta):
    min_distance = delta
    quicksort_with_key(points, 0, len(points) - 1, 1)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            if points[j][1] - points[i][1] >= min_distance:
                break
            min_distance = min(min_distance, distance(points[i], points[j]))
    return min_distance


def closest_pair(points):
    n = len(points)
    if n <= 3:
        return min(distance(points[i], points[j]) for i in range(n)
                   for j in range(i + 1, n))
    middle = n // 2
    left_points = points[:middle]
    right_points = points[middle:]

    delta_left = closest_pair(left_points)
    delta_right = closest_pair(right_points)
    delta = min(delta_left, delta_right)

    mid_x = points[middle][0]
    strip_points = [elem for elem in points if abs(elem[0] - mid_x) < delta]
    return round(min(delta, closest_pair_in_strip(strip_points, delta)), 6)


def task9():
    data = list(tuple(map(int, elem.split())) for elem in read_from_file()[1:])
    quicksort_with_key(data, 0, len(data) - 1, 0)
    write_in_file(str(closest_pair(data)))


if __name__ == "__main__":
    task9()
