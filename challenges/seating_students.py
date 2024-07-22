def SeatingStudents(arr):
    K, *occupied = arr

    count = 0

    for i in range(1, K, 2):
        left, right = i, i+1
        left_available = left not in occupied
        right_available = right not in occupied

        if left_available and right_available:
            count += 1

        if left_available and left + 2 not in occupied and left < K-1:
            count += 1

        if right_available and right + 2 not in occupied and right < K:
            count += 1

    return count


# keep this function call here
print(SeatingStudents(input()))
