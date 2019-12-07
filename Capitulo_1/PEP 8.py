# Avoiding the use of extra spaces
# Yes:
spam(ham[1], {eggs: 2})
# No:
spam( ham[ 1 ], { eggs: 2 } )

# Yes:
if x == 4: print x, y; x, y = y, x
# No:
if x == 4 : print x , y ; x , y = y , x


# Yes:
spam(1)
# No:
spam (1)

# Yes:
dct['key'] = lst[index]
# No:
dct ['key'] = lst [index]

# Yes:
x = 1
y = 2
long_variable = 3

# No:
x             = 1
y             = 2
long_variable = 3