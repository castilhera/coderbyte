def BracketMatcher(strParam):
    counter = 1

    for char in strParam:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1

            if not counter:
                return 0

    return 1 if counter == 1 else 0


# keep this function call here 
print(BracketMatcher(input()))
