listim = [1, 5, 'Hadjer', 50.3]
listim = listim[len(listim)//2:] + listim[:len(listim)//2]
print(listim)

n = int(input("Enter a single digit integer: "))
if n >= 0 and n < 10:
    for number in range(n+1):
        if number % 2 == 0:
            print(number)
else:
    print('Invalid number')
