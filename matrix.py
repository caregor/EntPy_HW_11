"""
    ---Task 3---
Создайте класс Матрица. Добавьте методы для:
    * вывода на печать,
    * сравнения,
    * сложения,
    * *умножения матриц
"""


class Matrix:
    """
    Represents a matrix and provides methods for basic matrix operations.
    """

    def __init__(self, rows, cols):
        """
        Initialize a new matrix.

        :param rows: Number of rows.
        :param cols: Number of columns.
        """
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def set_value(self, row, col, value):
        """
        Set the value at the specified row and column of the matrix.

        :param row: Row index.
        :param col: Column index.
        :param value: Value to set at the specified position.
        :raises IndexError: If the row or column index is out of bounds.
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Row or column index out of bounds")

    def get_value(self, row, col):
        """
        Get the value at the specified row and column of the matrix.

        :param row: Row index.
        :param col: Column index.
        :return: The value at the specified position.
        :raises IndexError: If the row or column index is out of bounds.
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Row or column index out of bounds")

    def print_matrix(self):
        """
        Print the matrix.
        """
        for row in self.data:
            print(" ".join(map(str, row)))

    def add(self, other):
        """
        Add another matrix to this matrix.

        :param other: Another matrix with the same dimensions as this matrix.
        :return: new matrix.
        :raises ValueError: If the matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def multiply(self, other):
        """
        Multiply this matrix by another matrix.

        :param other: Another matrix.
        :return: A new matrix.
        :raises ValueError: If the number of columns in this matrix is not equal to the number of rows in the other matrix.
        """
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self.data[i][k] * other.data[k][j]
                result.data[i][j] = dot_product

        return result

    def __eq__(self, other):
        """
        Compare two matrix.

        :param other: Another matrix to compare with.
        :return: True if the matrices are equal.
        """
        if not isinstance(other, Matrix):
            return False

        if self.rows != other.rows or self.cols != other.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False

        return True