from functools import reduce

def mat ( m , n , v = None ) :

	"""

		>>> mat( 0 , 3 , 1 )
		[]

		>>> mat( 5 , 0 , 1 )
		[[], [], [], [], []]

		>>> M = mat( 5 , 3 , 1 )
		>>> M
		[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

		>>> M[1][2] = 2
		>>> M
		[[1, 1, 1], [1, 1, 2], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

	"""

	return [ [ v ] * n for _ in range( m ) ]


def transpose ( M , n , m ) :

	"""

		>>> M = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
		>>> transpose( M , 2 , 3 )
		[[1, 4], [2, 5], [3, 6]]

	"""

	A = mat( m , n )

	for i , j in subscripts( 0 , m , 0 , n ) :

		A[i][j] = M[j][i]

	return A

def reverse( M ) :

	"""

		>>> M = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
		>>> reverse( M )
		>>> M
		[[6, 5, 4], [3, 2, 1]]

	"""
	for row in M : row.reverse( )
	M.reverse( )


def show ( matrix ) :

	"""

		>>> print( show( mat( 5 , 3 , 1 ) ) , end = "" )
		1 1 1
		1 1 1
		1 1 1
		1 1 1
		1 1 1

		>>> M = mat( 2 , 3 , 12 )
		>>> M[0][1] = M[1][2] = 1
		>>> print( show( M ) , end = "" )
		12  1 12
		12 12  1

	"""

	out = ""

	width = reduce( max , ( len( str( item ) ) for row in matrix for item in row ) , 0 )

	for row in matrix :

		fmt = " ".join( [ "%" + str( width ) + "s" ] * len( row ) )

		out += fmt % tuple( row )
		out += "\n"

	return out


def subscripts ( mi , mj , ni , nj ) :

	"""

		>>> list( subscripts( 1 , 3 , 2 , 5 ) )
		[(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4)]

	"""

	for i in range ( mi , mj ) :

		for j in range ( ni , nj ) :

			yield i , j


def parse ( lines ) :

	M = []

	"""

		>>> M = [ [ 1 , -2 , 3 ] , [ -4 , 5 , 6 ] ]
		>>> parse( show( M ).splitlines( ) ) == M
		True

	"""

	for line in lines :

		M.append( list( map( int , line.split( ) ) ) )

	m = len( M )
	n = 0 if m == 0 else len( M[0] )

	return M , m , n
