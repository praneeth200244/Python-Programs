# Creating a new file
f = open('17_abc.txt', 'w')

# Writing into a file
f.write("Hello Bengaluru")

# Closing a file
f.close()

# Opening the existing file
# f = open('17_abc.txt') 'r' is the default mode
f = open('17_abc.txt', 'r')

# Extracting the content of file
fileContent = f.read()
print(fileContent)

f.close()

f = open('17_abc.txt', 'a')
text = "Hello World"
f.write(text)
f.close

with open('abc.txt', 'a') as f:
    f.write("Hi Bengaluru")

with open('17_fileFunctions.txt', 'r') as f:
    print(type(f))
    print(f.read())
    print(f.tell())
    f.seek(10)
    print(f.tell())
    print(f.read(5))
    f.truncate(5)
    print(f.read())
