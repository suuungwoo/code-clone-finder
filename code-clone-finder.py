# A = [item for sublist in [input().split()
#                           for i in range()] for item in sublist]
# 世界中のソースコードを標準入力で受け取り，トークンのリストに
A = []
for i in range(2):
    Input = input().split()
    A.extend(Input)
# 予約語のリスト
B = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
     'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
newA = [0 for i in range(len(A))]
# 予約語に存在しないトークン(変数，関数名)を$に変換
for i, a in enumerate(A):
    if a not in B:
        newA[i] = "$"
    else:
        newA[i] = A[i]
# newAリスト×newAリストの比較結果を2次元配列に
C = [[0 for i in range(len(A))] for j in range(len(A))]
for i, a in enumerate(newA):
    for j, b in enumerate(newA):
        if a == b:
            C[i][j] = 1
# 斜めに連続して1が並んでいるときを出力
for i in range(len(C)-1):
    for j in range(len(C)-1):
        if C[i][j] == 1 and C[i+1][j+1] == 1 and i != j:
            print(A[i])
