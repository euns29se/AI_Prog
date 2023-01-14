def getTri():
    resultList = []
    for x in range(1,31):
        for y in range(1, 31):
            for z in range(1, 31):
                if z**2 == x**2 + y**2:
                    resultList.append((x, y, z))
    return resultList

result = getTri()
print(result)