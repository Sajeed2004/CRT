for i in range(1,5):
    for j in range(1,5):
        if(i+j<=4):
            print(" ",end="\t")
        else:
            print(j+(i-1)*4,end="\t")
    print()
    