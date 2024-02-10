def compte(t):
        cpt = 1
        for i in range(1,len(t)):
                if t[i] != t[i-1]:
                        cpt = cpt + 1
        return cpt