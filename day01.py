t = open('day_01.txt', 'r')
data = t.readlines()
one_string = ''.join(data)
pieces = one_string.split('\n\n')

sums = []
for i in pieces:
    t = i.split('\n')
    t = list(map(int, t))
    sums.append(sum(t))
print(max(sums))

# part 2
sums.sort(reverse=True)
sum(sums[0:3])
