

def perfect():
    i=1
    while i<1000:
        sum=0
        a=t
        while a>0:
            j=1
            k=1
            r=a%10
            while j<=r:
                k=k*i
                j=j*1
            sum=sum+k
            a=a//10
        if sum==a:
            print(sum,"perfect no")
        t=t+1
perfect()
