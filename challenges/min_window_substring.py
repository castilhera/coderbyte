from collections import Counter

def MinWindowSubstring(strArr):
    strN, strK = strArr
    strN_len = len(strN)
    strK_len = len(strK)

    sK = Counter(strK)

    while 1:
        for i in range(strK_len, strN_len + 1):
            window = strN[i-strK_len: i]
            found_min_window = True

            for char in sK.keys():
                if char not in window or window.count(char) < sK[char]:
                    found_min_window = False
                    break

            if found_min_window:
                return window

        strK_len += 1


# keep this function call here 
print(MinWindowSubstring(input()))
