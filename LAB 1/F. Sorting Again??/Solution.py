n = int(input())
lis1 = list(map(int,input().split()))
lis2 = list(map(int,input().split()))

tup_list = []
for i in range(n):
    tup_list.append((lis1[i],lis2[i]))

swap = 0

for i in range(n-1):
    max = i
    for j in range(i+1,n):
        if tup_list[j][1] > tup_list[max][1] or (tup_list[j][1] == tup_list[max][1] and 
        tup_list[j][0] < tup_list[max][0]):
            max = j
    if max != i:
        tup_list[max], tup_list[i] = tup_list[i], tup_list[max]
        swap += 1

print(f"Minimum swaps: {swap}")
for i in range(n):
    print(f"ID: {tup_list[i][0]} Mark: {tup_list[i][1]}")
