
from functools import reduce
from operator import mul
from random import sample

def C ( n , k ) :

	"""

		>>> C( 4 , 2 )
		6

		>>> C( 0 , 0 )
		1

		>>> C( -1 , 0 )
		0

	"""

	if n < 0 or k < 0 or n < k : return 0

	k = min( k , n - k )

	if k == 0 : return 1

	numer = reduce( mul , range( n , n - k , -1 ) )
	denom = reduce( mul , range( 1 , k + 1 ) )

	return numer // denom

def choose ( n , k ) :

	"""

		>>> A = choose( 10 , 3 )
		>>> len( A )
		3

		>>> sorted( choose( 10 , 10 ) )
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	"""

	return sample( range( n ) , k )

