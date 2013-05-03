def is_unique(string):
    checker = 0
    for ch in string:
        val = ord(ch) - ord('a')
        if checker & 1 << val > 0:
            return False
        checker |= 1 << val
    return True



if __name__ == "__main__":
    string = "hogefuba"
    print string, is_unique(string)
    string = "ppppe"
    print string, is_unique(string)
