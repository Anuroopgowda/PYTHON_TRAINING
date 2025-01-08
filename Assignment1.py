string = "A - 13, B - 14, C - 15"
# dict1={}
# lst=string.split(", ")
# print(lst)
# for val in lst:
#     dict1[val[0]]=val[4:]
# print(dict1)

# ----------------------------problem1------------------------

# dict1={val[0]:val[4:] for val in string.split(", ")}
# print(dict1)

# -----------------------------problem2-------------------------

# string = "11 - 13, 12 - 14, 13 - 15"
# dict1={int(val[:2]):int(val[4:]) for val in string.split(", ")}
# print(dict1)

# ------------------------------problem3------------------------

n_row=int(input("n:"))
matrix=[]
m_col=int(input("m:"))
for i in range(n_row):
    lst = list(map(int, input("element:").strip().split()))[:m_col]
    matrix.append(lst)
print(matrix)