import os
import sys
import heapq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab5.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))

def parallel_processing(flow_number, task_number, tasks):
    result = []
    priority_queue = [(0, i) for i in range(flow_number)]
    heapq.heapify(priority_queue)
    for i in range(task_number):
        finish_time, flow_index = heapq.heappop(priority_queue)
        result.append((flow_index, finish_time))
        heapq.heappush(priority_queue, (finish_time + tasks[i], flow_index))
    return result

def task5():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    flow_number, task_number = map(int, data[0].split())
    array = list(map(int, data[1].split()))
    result = "\n".join([f"{elem[0]} {elem[1]}" for elem in
                        parallel_processing(flow_number, task_number, array)])

    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task5()
