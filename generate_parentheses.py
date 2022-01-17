"""
Generate Valid Parentheses.
A combination that contains 1 type of parentheses is valid if every opening
parentheses has its closing parenthesis, and it doesn't have a closing parenthesis without
having an unused opening parenthesis before it.
"""
from typing import List


def generate(n) -> List:
    def rec(n, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n-1, diff+1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(n-1, diff-1, comb, combs)
            comb.pop()
    combs = []
    rec(2*n, 0, [], combs)
    return combs


if __name__ == '__main__':
    num = 3
    result = generate(num)
    print(f'The generated parentheses are: {result}')