s=input("enter the string:")
a = list(s)
vowels = ('a' , 'e' , 'i' ,  'o' , 'u' ,'A' ,'I', 'O' ,'U','E')
s1=""
i = 0
j = len(s) - 1
while i < j:
    if a[i] in vowels and a[j] in vowels:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    if a[i] not in vowels:
        i += 1
    if a[j] not in vowels:
        j -= 1
x=0
while x<len(a):
    s1+=a[x]
    x+=1
print(s1)