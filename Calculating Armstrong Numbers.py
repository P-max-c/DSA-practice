def isa(n):
    digit=str(n)
    s=len(digit)
    asu=sum(int(digit[i])**s for i in range(s))
    return asu==n

n=int(input(("Enter a number: ")))
if isa(n):
    print(f"{n} is an Armstrong number.")       
else:
    print(f"{n} is not an Armstrong number.")