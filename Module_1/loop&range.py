number=[5,10,15,20,25]
sum= 0
for num in number:
    print(num)
    sum+=num
    if sum>20:
        print('Bigger Sum',sum)
print('Sum = ',sum)

#Characters/String:
text = "Mad Man"
for char in text:
    print(char)

#Range:
for i in range(1,10):
    print(i)


for i in range(1,10,2):
    print(i)