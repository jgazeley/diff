from sys import argv

file1 = argv[1]
file2 = argv[2]

f1 = open(file1, 'rb')
f2 = open(file2, 'rb')

i = 0x0
b = True
result = ""

while(b):
  if f1.read(1) == b'' or f2.read(1) == b'':
    b = False
  f1.seek(i)
  f2.seek(i)
  if f1.read(16) == f2.read(16):
  	i += 0x10
  	f1.seek(i)
  	f2.seek(i)
  else:
  	result = "Files are not identical."
  	break

  result = "The files are identical."

print(result)
