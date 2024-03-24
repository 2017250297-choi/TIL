import random
import time


def test_time(func):
    def wrap(*args):
        st = time.time()
        func(*args)
        print(time.time() - st)

    return wrap


def solution1(ranks, attendance):
    participants = [x for x, y in zip(enumerate(ranks), attendance) if y]
    # [(0, 7), (1, 8), (2, 2), (3, 3), (4, 4), (5, 1), (6, 9), (7, 5), (8, 6)]
    sorted_ = sorted(participants, key=lambda x: x[1])  # nlogn
    return sorted_[0][0] * 10000 + sorted_[1][0] * 100 + sorted_[2][0]


def solution2(ranks, attendance):
    participants = [x for x, y in zip(enumerate(ranks), attendance) if y]
    result = 0
    for i in range(3):
        min_ = [101, 101]
        min_index = -1

        for index, row in enumerate(participants):
            if min_[1] > row[1]:
                min_ = row
                min_index = index
        result += 100 ** (2 - i) * min_[0]
        participants.pop(min_index)
    return result


input_arr = [x for x in range(1, 10)]
random.shuffle(input_arr)
input_arr2 = [True] * len(input_arr)
# print("----------------------1---------------")
# a = time.time()
# solution1(input_arr, input_arr2)
# print(time.time() - a)
# print("----------------------2---------------")
# a = time.time()
# solution2(input_arr, input_arr2)
# print(time.time() - a)


@test_time
def sol_float(edge, plain):
    # x^2 + A*x + B = 0
    # -A//2 +- ((A//2)**2 - B )**0.5
    A = (edge // 2 + 2) * -1
    B = edge + plain
    a, b = -A / 2 + ((A / 2) ** 2 - B) ** 0.5, -A / 2 - ((A / 2) ** 2 - B) ** 0.5
    return [a, b]


@test_time
def sol_b(edge, plain):
    FACE = edge + plain
    for i in range(1, 1 + int((FACE) ** 0.5)):
        if (FACE) % i == 0 and i - 2 + (FACE) // i == edge // 2:
            return [FACE // i, i]


sol_float(*[596, 20000])
sol_b(*[596, 20000])
