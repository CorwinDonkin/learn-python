p=0
x=1
while x==1:
    n=int(input("Input a number between 100 and 1000."))
    if n < 100 or n > 1000:
        break
        print(p,"primes")
    else:
        prime=True
        for i in range(2, n-1):
            r=n % i
            if r==0:
                prime=False
                break

        if prime==True:
            p=p+1
            print("It was prime.")
        else:
            print("It wasn't prime")