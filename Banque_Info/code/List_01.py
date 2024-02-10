def maxi(t):
    m = -1 
    for k in range(len(t)):
        if t[k] > m:
            m = t[k] 
    return m