def to_binary(n):
    result = []
    while n >= 1:
        b = n % 2
        result.append(b)
        n = n // 2

    return result


def rec_to_binary(n, result=None):
    if result is None:
        result = []
    if n > 1:
        rec_to_binary(n // 2, result)
    b = n % 2
    result.append(b)
    return result[::-1]
