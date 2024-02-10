def mystere(n) :
    if n % 3 == 0 or n % 5 == 0 :
        if n % 3 == 0 :
            resultat = 'A'
        else :
            resultat = 'B'
    else :
        if n % 5 == 0 :
            resultat = 'C'
        else :
            resultat = 'D'
    return resultat