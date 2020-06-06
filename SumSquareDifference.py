#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
natural = []
squares = []
nSum=0
sSum=0

for i in range (1,101):
    natural.append(i)
    squares.append(i*i)
    
print (natural)
print (squares)

for x in range (100):
    nSum+= natural[x]
    sSum+=squares[x]

print (nSum)
print (sSum)

sOfSum = nSum **2

print (sOfSum)

diff = sOfSum - sSum

print(diff)
