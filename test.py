# m1 = [[1, 0],[0, 1]]
# m2 = [[0, 2],[2, 0]]

# sr = [[0, 0],[0, 0]]
# dr = [[0, 0],[0, 0]]
# mr = [[0, 0],[0, 0]]
# tr = [[0, 0],[0, 0]]

# for i in range(len(m1)):
#     for j in range(len(m1[0])):
#         sr[i][j] = m1[i][j] + m2[i][j]

# for r in sr:
#     print(r)

# for i in range(len(m1)):
#     for j in range(len(m1[0])):
#         dr[i][j] = m1[i][j] - m2[i][j]

# for r in dr:
#     print(r)

# for i in range(len(m1)):        
#     for j in range(len(m2[0])):
#         for k in range(len(m2)):
#             mr[i][j] += m1[i][k] * m2[k][j]

# for r in mr:
#     print(r)

# for i in range(len(m1)):
#     for j in range(len(m1[0])):
#         tr[j][i] = m1[i][j]

# for r in tr:
#     print(r)

# arr=[1,2,3,4,5]
# target=3
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Found at index", i)
#         break
# else:
#     print("Not Found")



def binary_search(arr, x):
    l = 0
    h = len(arr) - 1
    mid = 0

    while l <= h:

        mid = (h + l) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr=[1,2,3,4,5]
target=3

result = binary_search(arr, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
