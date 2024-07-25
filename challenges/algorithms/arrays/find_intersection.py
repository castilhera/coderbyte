def FindIntersection(strArr):
    list1 = strArr[0].split(", ")
    list2 = set(strArr[1].split(", "))

    intersection = [num for num in list1 if num in list2]

    return ','.join(intersection) if intersection else "false"


# keep this function call here 
print(FindIntersection(input()))
