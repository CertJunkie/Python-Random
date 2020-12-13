print("Please enter a number")
n = int(input())

for row in range(1,n+1):
    for i in range (1,n+1):
        print(row*1,end="\t")
    print('')