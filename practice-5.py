### problem-1

### Reading a text file , consisting of some numbers , (make the text file on your own ).
#  Convert the numbers to a list , check to see list is palindromic or not.If it is , 
# then append "yes" to the list . If not , reweite the list with "0" 
# equal to the list length. close the file.

f = open('Numbers', 'w+')
f.write('123321')
f.close()

f = open("Numbers", 'r+')
someList = list(f.read())
f.close()


isPalindromic = True

for i in range(int(len(someList)/2)):
    if someList[i] != someList[len(someList)-i-1]:
        isPalindromic = False

if isPalindromic:
    f = open('Numbers','a')
    f.write('YES')
    f.close()

else:
    f = open('Numbers', 'w')
    for i in range(len(someList)):
        f.write('0')
        


