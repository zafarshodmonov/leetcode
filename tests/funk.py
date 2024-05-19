def restoreIpAddresses(s: str) -> list[str]:
    ans = []
    leng = len(s)
    def B(temp, ex, ind):
        if ex == 4:
            ans.append(temp[:-1])
            return
        y = leng - ind
        z = (4 - (ex + 1)) * 3
        for x in range(1, 4):
            if (y - x <= z) and (y - x >= 0):
                a = s[ind:ind+x]
                b = int(a)
                if x == 2 and 10 > b:
                    continue
                if x == 3 and 100 > b:
                    continue
                if x == 3:
                    if int(a) <= 255:
                        B(temp+a+".",ex+1,ind+x)
                else:
                    
                    a = s[ind : ind + x]+"."
                    B(temp+a, ex+1,ind+x)
    B("", 0,0)
    return ans
