friends = ["Jim", "Karen", "Kevin"]

for i in friends:
    print(i)

print('----')
for i in range(len(friends)):
    print(i)

print('----')

for i in range(10): # 0 - 10 not including 10
    print(i)

print('----')

for i in range(3,10):
    print(i)

for i in range(5):
    if i == 0:
        print("First iteration")
    else:
        print("Not first")

print('----')

for i in range(10):
    if i % 2 == 0:
        print("I am even,", end = ' ')
        print(i)
    else:
        print("I am odd,", end = ' ')
        print(i)
