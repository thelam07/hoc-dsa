def pascalTriangle(numRows: int) -> list[list[int]]:
    triangle = []
    triangle.append([1])
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle