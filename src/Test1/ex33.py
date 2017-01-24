i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    
print "The numbers: "

for num in numbers:
    print num
i = 0
numbers = []
    
def test(argument1, argument2):
    global i, numbers
    while i < argument1:
        print "At the top i is %d" % i
        numbers.append(i)      
        
        i = i + argument2
        print "Numbers now: ",numbers
        print "At the bottom i is %d" % i
test(100, 6)

print "The numbers: "
for num in numbers:
    print num