str1 = input('input str :')
count = int(input ( 'input caunt :'))
chars = [ord(char) for char in str1]
chars=[i+count for i in chars ]
chars = ''.join(chr(num) for num in chars)
print (chars)