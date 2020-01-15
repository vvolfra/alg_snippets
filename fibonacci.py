def fib(n):
	return int(((1+5**0.5)**n - (1-5**0.5)**n)/2**n/5**0.5)



def fib_last_digit(n):
	n %= 60
    return int(1/(5**0.5)*(((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n))%10
	
	
	
def fib_mod(n,m):
	arr,i=[0,1],2
	while not (arr[i-2]==0 and arr[i-1]==1) or i<=2:
		arr.append((arr[i-2]+arr[i-1])%m)
		i+=1
	return(arr[n%(i-2)])
