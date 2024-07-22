def QuestionsMarks(strParam):
    result = "false"
    num1 = -1
    qmarks_count = 0

    for char in strParam:
        if char.isdigit():
            num2 = int(char)
            if num1 + num2 == 10:
                if qmarks_count != 3:
                    return "false"
                result = "true"
            qmarks_count = 0
            num1 = num2
        elif char == '?':
            qmarks_count += 1
    return result


# keep this function call here 
print(QuestionsMarks(input()))
