#https://leetcode.com/problems/sliding-puzzle/description/
from collections import deque
from itertools import combinations
#0 1 2
#3 4 5
to_from = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

manhattan_table = {
    1: [0,1,2,1,2,3], 2: [1,0,1,2,1,2], 3: [2,1,0,3,2,1],
    4: [1,2,3,0,1,2], 5: [2,1,2,1,0,1], 0: [3,2,1,2,1,0]}

def manhattan(comb):
    res = 0
    for i,val in enumerate(comb):
        if val != 0:
            res += manhattan_table[val][i]
    return res

def inversions(comb):
    res = 0
    for i in combinations(range(6), 2):
        if comb[i[0]] > comb[i[1]] and comb[i[1]] != 0:
            res += 1
    return res

class Combination:
    def __init__(self, data, prev=None, step=0):
        self.data = data
        self.prev = prev
        self.step = step

    def __eq__(self, other):
        return all(a == b for a, b in zip(self.data, other.data))

    def next_step(self):
        res = []
        curr = self.data.index(0)
        directions = [direction for direction in to_from[curr] if direction != self.prev]
        for direction in directions:
            arr = list(self.data)
            arr[self.prev], arr[direction] = arr[direction], arr[self.prev]
            res.append(Combination(arr, prev=direction, step=self.step + 1))
        return res

def main():
    line = [[3,2,4],[1,5,0]]

    start = Combination([1,2,3,4,5,0], prev=5)
    final = Combination(line[0] + line[1])

    if inversions(final.data) % 2 == 1:
        print(-1)
    elif start == final:
        print(0)
    else:
        queue = deque([start])
        globe_table = [start]

        while len(queue):
            res = queue.popleft().next_step()
            for each in res:
                if each not in globe_table:
                    queue.append(each)
                    globe_table.append(each)
                if each == final:
                    print(each.step)
            if final in res:
                break



if __name__ == "__main__":
    main()
