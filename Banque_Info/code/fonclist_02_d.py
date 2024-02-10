def compte(t):
        cpt = 0
        for i in range(0,len(t)-1):
                cpt = cpt + int(t[i] != t[i+1])
        return cpt