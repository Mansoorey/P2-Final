def convert(n):
    if n <=0:
        print("Enter a positive Integer")
    if n == 1:
        return n
    else:
        convert(n//2)
        print(n)
n = int(input("Enter Number: "))
convert(n)


