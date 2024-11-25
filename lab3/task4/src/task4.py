from lab3.utils import read_from_file, write_in_file, quicksort_with_key

def count_points_in_segments(segments, points):
    start_end_points = list()
    point_count = dict()
    for elem in segments:
        start_end_points += [(elem[0], -1), (elem[1], 1)]
    for elem in points:
        start_end_points += [(elem, 0)]
        point_count[elem] = 0
    quicksort_with_key(start_end_points, 0, len(start_end_points) - 1, 1)
    quicksort_with_key(start_end_points, 0, len(start_end_points) - 1, 0)
    segments_count = 0
    for elem, elem_type in start_end_points:
        if abs(elem_type) == 1:
            segments_count += -elem_type
        else:
            point_count[elem] = segments_count
    return point_count.values()

def task4():
    data = read_from_file()
    segments = [list(map(int, elem.split())) for elem in data[1:-1]]
    points = list(map(int, data[-1].split()))
    write_in_file(" ".join(map(str, count_points_in_segments(segments, points))))


if __name__ == "__main__":
    task4()
