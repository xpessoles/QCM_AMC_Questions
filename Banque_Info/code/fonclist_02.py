def compte(t):
        cpt = 1
        for i in range(1,len(t)):
                if t[i] != t[i-1]:
                        cpt = cpt + 1
        return cpt

def compte(t):
        cpt = 1
        for i in range(0,len(t)-1):
                cpt = cpt + int(t[i] != t[i+1])
        return cpt

def compte(t):
        cpt = 0
        for i in range(0,len(t)-1):
                cpt = cpt + int(t[i] != t[i+1])
        return cpt

def compte(t):
        cpt = 0
        for i in range(0,len(t)-1):
                if t[i] != t[i+1]:
                        cpt = cpt + 1
        return cpt+1