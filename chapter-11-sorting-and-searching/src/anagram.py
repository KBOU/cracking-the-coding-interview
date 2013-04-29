# coding: utf-8

def anagram(arr, ch, num_done):
    if len(arr) == 1 or ord(ch) > ord("z"):
        return arr

    counts = {}
    for elem in arr:
        cnt = 0
        for s in elem:
            if s == ch:
                cnt += 1
        if counts.get(cnt):
            counts.get(cnt).append(elem)
        else:
            counts[cnt] = [elem]

    if len(counts) == 1:
        done = True
        for cnt, subarr in counts.items():
            for elem in subarr:
                if len(elem) > cnt + num_done:
                    done = False
                    break
        if done:
            return arr

    new_arr = []
    for cnt, subarr in counts.items():
        new_arr.extend(anagram(subarr, chr(ord(ch) + 1), num_done + cnt))

    return new_arr

if __name__ == "__main__":
    arr = ["abc", "add", "cba", "dda", "cbc", "ad", "da"]
    sorted_arr = anagram(arr, "a", 0)
    print sorted_arr
