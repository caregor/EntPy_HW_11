from matrix import Matrix


if __name__ == '__main__':
    matrix1 = Matrix.from_input(3, 3)
    matrix2 = Matrix.from_input(3, 3)

    print("Matrix 1:")
    matrix1.print_matrix()

    print("Matrix 2:")
    matrix2.print_matrix()

    result_matrix = matrix1.add(matrix2)
    print("Result of add:")
    result_matrix.print_matrix()

    print('Result mul:')
    result_matrix = matrix1.multiply(matrix2)
    result_matrix.print_matrix()