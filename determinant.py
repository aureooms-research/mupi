
from numbers import gcd , prod

def det ( A , n ) :

	"""

		Using Gaussian elimination and gcd. For integers only!

		>>> det( [ [ 4 , 1 ] , [ 1 , 2 ] ] , 2 )
		7

		>>> det( [ [ -2 , 2 , -3 ] , [ -1 , 1 , 3 ] , [ 2 , 0 , -1 ] ] , 3 )
		18

		>>> det( [ [ -1 , 1 , 3 ] , [ -2 , 2 , -3 ] , [ 2 , 0 , -1 ] ] , 3 )
		-18

	"""

	d = 1

	for i in range ( n - 1 ) :

		# find first non zero row

		if A[i][i] == 0 :

			j = i + 1

			while j < n :

				if A[j][i] != 0 : break

				j += 1

			if j == n : return 0

			# make it the ith row

			A[i] , A[j] = A[j] , A[i]

			d = -d

		for j in range ( i + 1 , n ) :

			a = A[i][i]
			b = A[j][i]

			c = gcd( a , b )

			a //= c
			b //= c

			# we want to cancel A[j][i]

			# assert  a * A[j][i] == b * A[i][i]

			A[j][i] = 0

			# so we multiply both rows so that
			#
			#     A[i][i] = A[j][i] = lcm( A[i][i] , A[j][i] )
			#
			# and we remove the ith row from the jth row

			for k in range ( i + 1 , n ) :

				A[j][k] = a * A[j][k] - b * A[i][k]

			d *= a

	return prod( A[i][i] for i in range( n ) ) // d
