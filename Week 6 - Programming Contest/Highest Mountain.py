number = int(input())
for a in range(1, number+1):
    r = input()
    l = int(input())
    ls = input().split(" ")
    ls = [int(i) for i in ls]
    x = ls[0]
    if x == 1:
        height = 1
        index = 0
        plus = True
    else:
        big = 0
        height = -1
        index = -1
        plus = False
    for i in range(1,len(ls)):
        if plus and ls[i]-ls[i-1] == 1:
            big = i
            continue
        elif ls[i]-ls[i-1] == -1:
            if plus:
                if ls[i-1] > height:
                    height = ls[i-1]
                    index = i-1
                    plus = False
            elif ls[i] == 1:
                plus = True
                if ls[big] > height:
                    height = ls[big]
                    index = big
        elif ls[i] == 1:
            big = i
            plus = True
        else:
            big = i
            if plus:
                plus = False
                if ls[i-1] > height:
                    height = ls[i-1]
                    index = i-1
    else:
        if plus:
            if ls[-1] > height:
                height = ls[-1]
                index = l-1

    print("Case #{}: {} {}".format(a,height,index))
