variable_1 = 1

def scope_training ():
    variable_2 = 2


def scope_training_2 ():
    variable_1 = 10
    print (variable_1)


#print (variable_2) #Not possible

scope_training_2 ()
print (variable_1)