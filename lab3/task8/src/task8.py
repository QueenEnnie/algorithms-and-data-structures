from lab3.utils import read_from_file, write_in_file, quicksort_with_key
from math import sqrt

def find_closet_to_origin(coordinates, number_out):
    distance_coordinates = [[sqrt(x ** 2 + y ** 2), (x, y)] for x, y in coordinates]
    quicksort_with_key(distance_coordinates, 0, len(distance_coordinates) - 1, 0)
    return [elem[1] for elem in distance_coordinates[:number_out]]

def task8():
    data = read_from_file()
    number_out = int(data[0].split()[1])
    coordinates = [(int(elem.split()[0]), int(elem.split()[1])) for elem in data[1:]]
    out = [f"[{elem[0]},{elem[1]}]" for elem in find_closet_to_origin(coordinates, number_out)]
    write_in_file(",".join(out))

if __name__ == "__main__":
    task8()
