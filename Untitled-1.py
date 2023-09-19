import random
A = [random.randrange(0, 1000000000) for i in range(0, 1000001)]
def solution(A):
    count = {}
    for num in A:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num in count:
        if count[num] == 1:
            return num
    return -1
print(solution(A))

        