#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    return ([list(map(lambda x: x * x, row)) for row in matrix])
=======
	return [list(map((lambda x: x * x), elm)) for elm in matrix]
>>>>>>> 33efbdfc84f3512909b62d681c4cafe873af1367
