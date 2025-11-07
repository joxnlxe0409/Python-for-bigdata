f = open('hello.txt', 'w')
f.write("Hello World!")
f.close() 

f = open('hello.txt', 'r')
s = f.read()
print(s)
f.close()