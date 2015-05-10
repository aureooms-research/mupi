
from matrix import subscripts
from combinatorics import choose

def info ( M , m , n ) :

	# fill M
	# we assume that for all j > i --> ai < aj and bi < bj
	# M[i][j] = -1 means ai < bj
	# M[i][j] =  1 means ai > bj
	# M[i][j] =  0 means ai and bj are incomparable

	# generate random info

	positions = sorted( choose( m + n , m ) )

	for i , j in enumerate( positions ) :

		M[i][:j-i] = [  1 ] * ( j - i )
		M[i][j-i:] = [ -1 ] * ( n - j + i )

	return M


def fix ( M , m , n ) :

	"""

		>>> M = [ [ -1 , -1 ] , [ 1 , 1 ] ]
		>>> fix( M , 2 , 2 )
		>>> M
		[[-1, -1], [1, 1]]
		>>> M = [ [ -1 , 0 ] , [ 0 , 1 ] ]
		>>> fix( M , 2 , 2 )
		>>> M
		[[-1, -1], [1, 1]]
		>>> M = [ [ 0 , 0 , 0 ] , [ -1 , -1 , -1 ] ]
		>>> fix( M , 2 , 3 )
		>>> M
		[[-1, -1, -1], [-1, -1, -1]]
		>>> M = [ [ 0 , 0 , 0 ] , [ 1 , 1 , 1 ] ]
		>>> fix( M , 2 , 3 )
		>>> M
		[[0, 0, 0], [1, 1, 1]]
		>>> M = [ [ -1 , -1 , -1 ] , [ 0 , 0 , 0 ] ]
		>>> fix( M , 2 , 3 )
		>>> M
		[[-1, -1, -1], [0, 0, 0]]
		>>> M = [ [ 1 , 1 , 1 ] , [ 0 , 0 , 0 ] ]
		>>> fix( M , 2 , 3 )
		>>> M
		[[1, 1, 1], [1, 1, 1]]

	"""

	# fix transitivity

	for i in range ( m ) :

		hi , lo = n , 0

		for j in range( n ) :

			if M[i][j] > 0 :
				lo = j

			elif M[i][j] < 0 :
				hi = j
				break

		for j in range( lo ) : M[i][j] = 1
		for j in range( hi , n ) : M[i][j] = -1

	for j in range ( n ) :

		hi , lo = m , 0

		for i in range( m ) :

			if M[i][j] < 0 :
				lo = i

			elif M[i][j] > 0 :
				hi = i
				break

		for i in range( lo ) : M[i][j] = -1
		for i in range( hi , m ) : M[i][j] = 1


def comparator ( M ) :

	"""
		>>> from matrix import mat
		>>> M = mat( 3 , 2 )
		>>> compare = comparator( M )
		>>> for i , j in subscripts( 0 , 3 , 0 , 2 ) : M[i][j] = 2 * i + j
		>>> compare( 0 , 0 ) == M[0][0]
		True
		>>> compare( 0 , 1 ) == M[0][1]
		True
		>>> compare( 1 , 0 ) == M[1][0]
		True
		>>> compare( 1 , 1 ) == M[1][1]
		True
		>>> compare( 2 , 0 ) == M[2][0]
		True
		>>> compare( 2 , 1 ) == M[2][1]
		True

	"""

	def compare ( i , j ) :

		return M[i][j]

	return compare

class Oracle ( object ) :

	def __init__ ( self , M ) :

		self.M = M
		self.count = 0

	def __call__ ( self , i , j ) :

		self.count += 1
		return self.M[i][j]

	def __len__ ( self ) :

		return self.count


def main ( m , n ) :

	from matrix import mat , show

	M = mat( m , n )
	info( M , m , n )
	print( show( M ) , end = "" )


if __name__ == "__main__" :

	import sys

	main( *map( int , sys.argv[1:] ) )
