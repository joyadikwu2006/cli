buy = []

buy.append("joy")
buy.append("john")
buy.append("mary")
index = 0
k = 1


rev = []

while index < 2:
    rev.append(buy[k])
    k -= 1
    index += 1

k = 1

rev.extend(buy[k+1:])

print(rev)

# buy.pop()

# print(buy)

# print("TOP item:", buy[-1])