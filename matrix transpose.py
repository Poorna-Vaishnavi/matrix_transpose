
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)


transpose = []
for j in range(cols):
    transposed_row = []
    for i in range(rows):
        transposed_row.append(matrix[i][j])
    transpose.append(transposed_row)


for row in transpose:
    print(row)
