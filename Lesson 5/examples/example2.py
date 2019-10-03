def round(num, ndigits=0):
    r = num % 1

    if not ndigits:
        if r >= 0.5:
            return num // 1 + 1

        return num // 1

    r_str = str(r).split('.')[-1]

    if len(r_str) < ndigits:
        return num

    st = int(r_str[ndigits:]) / 10 ** len(r_str)
    num = num - st

    if int(r_str[ndigits]) >= 5:
        num += 1 / 10 ** ndigits

    return num
