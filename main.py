import re

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def print_optimal_parentheses(s, i, j, matrix_names):
    if i == j:
        print(matrix_names[i], end='')
    else:
        print('(', end='')
        print_optimal_parentheses(s, i, s[i][j], matrix_names)
        print_optimal_parentheses(s, s[i][j] + 1, j, matrix_names)
        print(')', end='')

def main(matrix_file):
    with open(matrix_file, 'r') as file:
        matrix_data = file.read()

    matches = re.findall(r'\{\s*(\d+)\s*,\s*(\d+)\s*\}', matrix_data)
    dims = [int(match[0]) for match in matches]
    dims.append(int(matches[-1][1]))

    matrix_names = [f"M{i + 1}" for i in range(len(dims) - 1)]

    m, s = matrix_chain_order(dims)

    print("Minimum number of multiplications:", m[0][-1])
    print("Optimal Parentheses:")
    print_optimal_parentheses(s, 0, len(dims) - 2, matrix_names)
    print()

if __name__ == "__main__":
    matrix_file = "10.txt"  # Update this with the path to your input file
    main(matrix_file)
