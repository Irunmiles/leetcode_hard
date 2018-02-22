#https://leetcode.com/problems/remove-invalid-parentheses/description/
from itertools import combinations

def balance(line):
    bln = 0
    for ch in line:
        if ch == '(':
            bln += 1
        elif ch == ')':
            bln -= 1
        if bln < 0:
            return False
    return bln == 0

def check_combination(line, indexes):
    #we check only those paretheses which positions are enlisted in indexes

    balance = 0
    flag = True
    for i,character in enumerate(line):
        if i in indexes: #ignore some positions
            continue
        if character == '(':
            balance += 1
        elif character == ')':
            balance -= 1
        if balance < 0:
            flag = False
    return flag and balance == 0

def get_indexes(line, opening, closing):
    #we need positions of opening parentheses and closing ones to make a proper search 

    bln = 0
    for i,character in enumerate(line):
        if character == '(':
            opening += [i]
            bln += 1
        if character == ')':
            closing += [i]
            bln -= 1
    return bln

def compress(line, indexes):
    res = [ch for i,ch in enumerate(line) if i not in indexes]
    return "".join(res)

def remove_bracket(line):
    #returns all possible cases without one closing parenthesis

    closing = []
    get_indexes(line, [], closing)
    res = set()
    for each in closing:
        res.add(compress(line, [each]))
    return tuple(res)

def recursion_line(begin, line, variations):
    #idea:
    # a: 'begin' is a part of our line with a proper balance condition.
    # b: if bln moves down (bln == -1) we need to remove only one ')' from a whole previous part
    # c: whole line = begin + line
    # d: 'variations': we store there all possible lines with proper balance condition

    if line == "":
        variations.update({begin})
    else:
        curr, end, bln = 0, len(line), 0,
        while curr < end:
            if line[curr] == '(':
                bln += 1
                curr += 1
            elif line[curr] == ')':
                bln -= 1
                curr += 1
            else:
                curr += 1

            if bln == -1:
                new_lines = remove_bracket(begin + line[:curr])
                for each in new_lines:
                    recursion_line(each, line[curr:], variations)
                return None

        variations.update({begin+line})

def core_method(line, result):
    #we call it for every element from 'variations' from recursion_line
    #it works for cases bln != 0

    opening, closing = [], []
    bln = get_indexes(line, opening, closing)
    res = set()
    if bln < 0:	
        for combination in combinations(closing, -bln):
            if check_combination(line, combination):
                new_line = compress(line, combination)
                res.update({new_line}) 

    elif bln >0:
        for combination in combinations(opening, bln):
            if check_combination(line, combination):
                new_line = compress(line, combination)
                res.update({new_line})

    result += list(res)

def main():

    line = "()()()())r))))"
    output = set()

    if balance(line):
        output.add(line)
    else:
        variations = set()
        recursion_line("", line, variations)
        for each in variations:
            if balance(each):
                output.update({each})
            else:
                result = []
                core_method(each, result)
                output.update(result)

    print(list(output))



if __name__ == "__main__":
    main()