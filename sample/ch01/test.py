s = 7.66
e = 10.21
st = (10.21 - 7.66)/11
l = [s]
m = [7.66, 9.36, 8.94, 9.36, 8.94, 7.66, 8.51, 8.94, 9.36, 9.79, 10.21]
for x in range(1,12):
	s = s + st
	l.append(s)

print(sum(l))
print(sum(m))