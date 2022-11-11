first, second, third, fourth = input().split()
sec = second.split()
four = fourth.split()
if len(four) > len(third):
    print("No")
else:
    diff_cus = list(set(four) - set(sec))
    diff_shop = list(set(sec) - set(four))
    if len(diff_cus) == 0:
        print("Yes")
    else:
        for i in diff_cus:
            for j in diff_shop:
                if j > i:
                    diff_cus.remove(i)
                    break
        if len(diff_cus) == 0:
            print("Yes")
        else:
            print('No')
