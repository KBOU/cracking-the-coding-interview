def permutation(string1, string2):
    counts = {}
    for c in string1:
        cnt = counts.get(c,0)
        counts[c] = cnt+1

    for c in string2:
        cnt = counts.get(c, 0)
        cnt -= 1
        if cnt < 0:
            return False
        counts[c] = cnt
    return True

if __name__ == "__main__":
    string1 = "hoge"
    string2 = "geho"
    string3 = "hoga"
    print string1, string2, permutation(string1, string2)
    print string2, string3, permutation(string2, string3)
    print string1, string3, permutation(string1, string3)
