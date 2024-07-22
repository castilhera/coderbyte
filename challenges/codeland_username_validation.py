def CodelandUsernameValidation(strParam):
    # 1. The username is between 4 and 25 characters.
    if not 3 < len(strParam) < 26:
        return "false"

    # 2. It must start with a letter.
    if not strParam[0].isalpha():
        return "false"

    # 4. It cannot end with an underscore character.
    if strParam[-1] == '_':
        return "false"

    # 3. It can only contain letters, numbers, and the underscore character.
    for char in strParam:
        if not (char.isalnum() or char == '_'):
            return "false"
    
    return "true"


# keep this function call here 
print(CodelandUsernameValidation(input()))
