lis1 = input().split(" ")
inp_list = input().split(" ")
out_list = int(lis1[0])*[0]
for i in range(len(out_list)):
    out_list[i] = int(inp_list[len(inp_list)-i-1])
for i in range(int(lis1[0])-int(lis1[1]),len(out_list),1):
    if i == len(out_list)-1:
        print(out_list[i])
    else:
        print(out_list[i], end=" ")
