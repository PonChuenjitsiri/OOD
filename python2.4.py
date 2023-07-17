lstnum = input("Enter Your List : ").split()
res = []
if len(lstnum) > 2:
    found_combination = False
    for i in range(len(lstnum)):
        for j in range(i+1, len(lstnum)):
            for k in range(j+1, len(lstnum)):
                num1 = int(lstnum[i])
                num2 = int(lstnum[j])
                num3 = int(lstnum[k])
                if num1 + num2 + num3 == 0:
                    combo = sorted([num1, num2, num3])
                    if combo not in res:
                        res.append(combo)
                        found_combination = True
    
    
    print(res)
    
else:
    print("Array Input Length Must More Than 2")
