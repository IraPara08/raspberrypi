import os

def solve(s):
    name = s.split()
    capitalizedname = []
    for x in name:
        capitalizedname.append(x.capitalize())
    return ' '.join(capitalizedname)


if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
