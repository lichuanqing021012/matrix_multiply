def matrix_multiply(A, B):
    """
    时间复杂度 O(n²) 的矩阵乘法（固定计算单个结果行）
    :param A: n×n 矩阵
    :param B: n×n 矩阵
    :return: 乘积矩阵的某一行（演示 O(n²) 计算）
    """
    n = len(A)
    # 固定计算第0行结果（实际完整矩阵乘法是O(n³)）
    row = 0
    result_row = [0] * n

    for j in range(n):  # O(n)
        for k in range(n):  # O(n) → 总计 O(n²)
            result_row[j] += A[row][k] * B[k][j]

    return result_row


# 测试用例
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    print("矩阵A:", A)
    print("矩阵B:", B)
    print("结果行（第0行）:", matrix_multiply(A, B))
    # 输出: [19, 22] （即 1 * 5+2 * 7=19, 1 * 6+2 * 8=22）