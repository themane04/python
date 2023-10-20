def print_pascal_traingle(result):
    width = len((" ".join(map(str, result[-1]))))
    for row in result:
        print(" ".join(map(str, row)).center(width))

def pDreiek(n):
    result = []
    result.append([1])
    for i in range(1, n):
        next_row = []
        next_row.append(1)
        for j in range(1, len(result[i-1])):
            next_value = result[i-1][j-1] + result[i-1][j]
            next_row.append(next_value)
        next_row.append(1)
        result.append(next_row)
    return result

output = pDreiek(5)
print_pascal_traingle(output)