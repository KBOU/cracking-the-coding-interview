# coding: utf-8

def parse_exp(exp, res, okcounts):
    if exp == "1":
        okcounts.append(1) if res else okcounts.append(0)
        return
    elif exp == "0":
        okcounts.append(1) if not res else okcounts.append(0)
        return

    cnt = 0
    for i,ch in enumerate(exp):
        left_ok = []
        right_ok = []
        left_ng = []
        right_ng = []
        if exp[i] == "&":
            if res:
                parse_exp(exp[:i], res, left_ok)
                if left_ok[0] > 0:
                    parse_exp(exp[(i+1):], res, right_ok)
                    cnt += (left_ok[0] * right_ok[0])
            else:
                parse_exp(exp[:i], True, left_ok)
                parse_exp(exp[:i], False, left_ng)
                parse_exp(exp[(i+1):], True, right_ok)
                parse_exp(exp[(i+1):], False, right_ng)

                cnt += ((left_ok[0] + left_ng[0]) * (right_ok[0] + right_ng[0]) - left_ok[0] * right_ok[0])
        elif exp[i] == "|":
            if res:
                parse_exp(exp[:i], True, left_ok)
                parse_exp(exp[:i], False, left_ng)
                parse_exp(exp[(i+1):], True, right_ok)
                parse_exp(exp[(i+1):], False, right_ng)

                cnt += ((left_ok[0] + left_ng[0]) * (right_ok[0] + right_ng[0]) - left_ng[0] * right_ng[0])
            else:
                parse_exp(exp[:i], res, left_ng)
                if left_ng[0] > 0:
                    parse_exp(exp[(i+1):], res, right_ng)
                    cnt += (left_ng[0] * right_ng[0])
        elif exp[i] == "^":
            parse_exp(exp[:i], True, left_ok)
            parse_exp(exp[:i], False, left_ng)
            parse_exp(exp[(i+1):], True, right_ok)
            parse_exp(exp[(i+1):], False, right_ng)
            if res:
                cnt += (left_ok[0] * right_ng[0]) + (left_ng[0] * right_ok[0])
            else:
                cnt += (left_ok[0] * right_ok[0]) + (left_ng[0] * right_ng[0])
    okcounts.append(cnt)
    return

if __name__ == "__main__":
    exp = "1^0|0|1^1&1"
    res = False
    okcounts = []
    parse_exp(exp, res, okcounts)
    print okcounts[0]
