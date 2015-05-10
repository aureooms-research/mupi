from matrix import mat , show , subscripts , parse
from information import comparator , Oracle
from math import log
from dynamic import tableau

def merge ( partial , P , oracle , e , m , n , verbose = 0 ) :

	i = m
	j = n

	while i > 0 and j > 0 :

		if verbose >= 2 :
			callback( "partial information" , i , j )
			callback( show( P ) , end = "" )
			callback( "tableau" , i , j )
			callback( show( e ) , end = "" )

		# A_m > B_n
		if partial( i - 1 , j - 1 ) > 0 :

			if verbose >= 2 : callback( "I know that A_m > B_n, so I output A_m and decrease m" )
			yield "a[%d]" % i
			i -= 1

		# A_m < B_n
		elif partial( i - 1 , j - 1 ) < 0 :

			if verbose >= 2 : callback( "I know that A_m < B_n, so I output B_n and decrease n" )
			yield "b[%d]" % j
			j -= 1

		# e(P(A_m < B_n)) / e(P) > 2/3
		# =>
		# e(P(B_n < A_m)) / e(P) < 1/3
		elif 3 * e[i-1][j] < e[i][j] :

			if verbose >= 2 : callback( "A_m > B_n with probability < 1/3" )

			t = 1

			while partial( i - 1 , t - 1 ) > 0 : t += 1

			r = t

			# By Linial's theorem we are guaranteed to break out this loop.

			while not e[i][j] <= 3 * e[i][r-1] <= 2 * e[i][j] : r += 1

			if oracle( i - 1 , r - 1 ) < 0 :

				while j >= r :
					yield "b[%d]" % j
					j -= 1

			else :

				while t <= r :
					P[i-1][t-1] = 1 # update partial information
					e[i][t] = e[i-1][t] # update lin. ext. count
					t += 1

				while t <= j :
					e[i][t] = e[i-1][t] # update lin. ext. count
					t += 1

		# e(P(A_m < B_n)) / e(P) < 1/3
		elif 3 * e[i][j-1] < e[i][j] :

			if verbose >= 2 : callback( "A_m < B_n with probability < 1/3" )

			t = 1

			while partial( t - 1 , j - 1 ) < 0 : t += 1

			r = t

			# By Linial's theorem we are guaranteed to break out this loop.

			while not e[i][j] <= 3 * e[r-1][j] <= 2 * e[i][j] : r += 1

			if oracle( r - 1 , j - 1 ) > 0 :

				while i >= r :
					yield "a[%d]" % i
					i -= 1

			else :

				while t <= r :
					P[t-1][j-1] = -1 # update partial information
					e[t][j] = e[t][j-1] # update lin. ext. count
					t += 1

				while t <= i :
					e[t][j] = e[t][j-1] # update lin. ext. count
					t += 1

		else :

			# we can simply compare A_m with B_n

			P[i-1][j-1] = oracle( i - 1 , j - 1 )

	while i > 0 :
		yield "a[%d]" % i
		i -= 1

	while j > 0 :
		yield "b[%d]" % j
		j -= 1




def main ( partial , total , verbose ) :

	P , m , n = parse( partial )

	if verbose >= 2 :

		print( "partial information" )
		print( show( P ) , end = "" )

	T , m , n = parse( total )

	oracle = Oracle( T )

	if verbose >= 2 :

		print( "total information" )
		print( show( T ) , end = "" )

	partial = comparator( P )

	e = tableau( partial , m , n )

	ITLB = log( e[m][n] , 2 )

	print( *list( reversed( list( merge( partial , P , oracle , e , m , n , verbose ) ) ) ) , sep = " < " )

	if verbose :

		print( "total queries :" , len( oracle ) )

		print( "n / ITLB :" , len( oracle ) / ITLB )

		print( "n / 1.44.. ITLB :" , len( oracle ) / ITLB * log((1+5**(1/2))/2,2) )


if __name__ == "__main__" :

	import sys , fileinput , argparse

	parser = argparse.ArgumentParser(description='Merge A and B.')
	parser.add_argument('poset', metavar='P' , help='the partial information to use')
	parser.add_argument('oracle', metavar='T' , help='the oracle')
	parser.add_argument('-v' , '--verbose', default = 0 , action='count', help='make output verbose')

	args = parser.parse_args( )

	main( fileinput.input( [ args.poset ] ) , fileinput.input( [ args.oracle ] ) , args.verbose )
