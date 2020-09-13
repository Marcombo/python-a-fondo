# Evitando el uso de espacios extra
# Bien:
spam(ham[1], {eggs: 2})
# Mal:
spam( ham[ 1 ], { eggs: 2 } )

# Bien:
if x == 4: print x, y; x, y = y, x
# Mal:
if x == 4 : print x , y ; x , y = y , x


# Bien:
spam(1)
# Mal:
spam (1)

# Bien:
dct['key'] = lst[index]
# Mal:
dct ['key'] = lst [index]

# Bien:
x = 1
y = 2
variable_larga = 3

# Mal:
x              = 1
y              = 2
variable_larga = 3