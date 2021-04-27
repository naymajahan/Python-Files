### OPEN A FILE

f = open('a.text', 'w')

### getting some infos

print('name = ', f.name)
print('is it closed ? ', f.closed)
print('mode = ', f.mode)
f.write('Python is my favorite language.')
f.close()


### appending to a file 
f = open('a.text', 'a')
f.write('I also love Java')
f.close()



## r+ functionality
f = open('a.text', 'r+')
info = f.read()
print(info)
f.close()

### read till certain chacter 
f = open('a.text', 'r+')
info = f.read(13)
print(info)
f.close()



#### w+ mode 
f = open('a.text', 'w+')
f.write('All is Lost')
f.close()


