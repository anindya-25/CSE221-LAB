T = int(input())
for i in range(T):
    lis = input().split(" ")
    if lis[2] == "+":
        print(f"{int(lis[1]) + int(lis[3]):.6f}")
    elif lis[2] == '-':
        print(f"{int(lis[1]) - int(lis[3]):.6f}")
    elif lis[2] == '*':
        print(f"{int(lis[1]) * int(lis[3]):.6f}")
    elif lis[2] == '/':
        print(f"{int(lis[1]) / int(lis[3]):.6f}")
