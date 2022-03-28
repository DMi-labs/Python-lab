print()
print()
print("                                                              MULTIPLICATION TIME TABLE CHART")
print()
print()

X = 1
Y = 1



for X in range(0,13):
    print('  '.format(X), end='   ')
    while Y <= 6:
        print('\t {:d} X {:d} = {:d}   '.format(Y,X, X *Y), end='\t')

        Y+=1
    print()
    Y=1

Y = 7

print()
print()
for X in range(0,13):
    print(' '.format(X), end=' ')
    while Y <= 12:
        print('\t{:d} X {:d} ={:d}  '.format(Y,X, X *Y), end='\t')

        Y+=1
    print()
    Y=7
    
print()
print()
print()

print ("                                                               Good Bye Friend !!!")
print()
print()
print ( "--Licensed By Sagacc--")
print ()    
