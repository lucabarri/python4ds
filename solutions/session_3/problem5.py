def binary_search(x, x_0):
    """Searches for x_0 in x."""
    # Left extremity
    left = 0
    # Right extremity
    right = len(x) - 1

    while left <= right:
        n_elems = right - left
        midpoint = left + n_elems // 2
        x_m = x[midpoint]

        # Checks if we found
        if x_m == x_0:
            return midpoint
        else:
            if x_m < x_0:
                # x_0 is on the right part
                left = midpoint + 1
            else:
                # x_0 is on the left part
                right = midpoint - 1
    return -1


def rec_binary_search(x, x_0, left=None, right=None):
    """Searches for x_0 in x recursively."""
    if left is None:
        left = 0
    if right is None:
        right = len(x) - 1

    if right >= 1:
        n_elems = right - left
        midpoint = left + n_elems // 2
        x_m = x[midpoint]

        if x_m == x_0:
            return midpoint
        else:
            if x_m < x_0:
                # x_0 is on the right part
                return rec_binary_search(x, x_0,
                                         left=midpoint + 1,
                                         right=right)
            if x_m > x_0:
                # x_0 is on the lef part
                return rec_binary_search(x, x_0,
                                         left=left,
                                         right=midpoint + 1)
    else:
        return -1
