from math import inf
def divide (first, second):
    if second == 0:
        return print(inf)
    if second > 0:
        result = int(first)/int(second)
        print(result)