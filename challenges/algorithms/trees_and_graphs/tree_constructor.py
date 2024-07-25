def TreeConstructor(strArr):
    parents = {}
    children = {}

    for node_str in strArr:
        child, parent = node_str[1:-1].split(',')

        if child == parent:
            return "false"

        if parent in parents:
            if len(parents[parent]) == 2:
                return "false"
            parents[parent].append(child)
        else:
            parents[parent] = [child]

        if child in children:
            return "false"
        else:
            children[child] = parent
    
    root = 0
    for parent in parents:
        if parent not in children:
            if root == 1:
                return "false"
            root += 1

    return "true"


# keep this function call here 
print(TreeConstructor(input()))
