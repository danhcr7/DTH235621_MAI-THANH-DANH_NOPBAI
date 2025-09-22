# Nhập ma trận từ bàn phím
def nhap_matrix(rows, cols, name):
    print(f"Nhập ma trận {name} ({rows}x{cols}):")
    M = []
    for i in range(rows):
        row = list(map(int, input().split()))
        while len(row) != cols:  # đảm bảo nhập đủ cột
            print(f"⚠️ Hàng {i+1} phải có {cols} phần tử. Nhập lại:")
            row = list(map(int, input().split()))
        M.append(row)
    return M

# In ma trận cho đẹp
def in_matrix(M, name="Matrix"):
    print(f"\n{name}:")
    for row in M:
        print(row)

# Cộng ma trận
def cong_matrix(A, B):
    rows, cols = len(A), len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

# Hoán vị ma trận (transpose)
def transpose(M):
    rows, cols = len(M), len(M[0])
    return [[M[j][i] for j in range(rows)] for i in range(cols)]

# --- MAIN ---
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

A = nhap_matrix(rows, cols, "A")
B = nhap_matrix(rows, cols, "B")

# Cộng A+B
C = cong_matrix(A, B)

# Hoán vị A và B
AT = transpose(A)
BT = transpose(B)

# In kết quả
in_matrix(A, "A")
in_matrix(B, "B")
in_matrix(C, "A + B")
in_matrix(AT, "A^T (Transpose của A)")
in_matrix(BT, "B^T (Transpose của B)")
