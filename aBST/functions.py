
def GenerateBBSTArray(a: list) -> list:
    bst_length = len(a)

    if bst_length == 0:
        return []

    if bst_length == 1:
        return a

    a = sorted(a)
    stack = []
    stack.append((0, bst_length // 2, None))  # (index_bst, parent, prev_parent)
    aBST = [None] * bst_length

    while stack:
        index_bst, parent, prev_parent = stack.pop(0)
        aBST[index_bst] = a[parent]

        if prev_parent is not None:
            distance_to_new_parrent = (parent - prev_parent) // 2

        if prev_parent is None:
            left =  parent // 2
            right =  parent + (parent - left)
        elif parent > prev_parent:
            left =  parent - distance_to_new_parrent
            right = parent + distance_to_new_parrent
        else:
            left =  parent + distance_to_new_parrent
            right = parent - distance_to_new_parrent

        left_index_bst = index_bst * 2 + 1
        right_index_bst = index_bst * 2 + 2
        prev_parent = parent

        if left_index_bst < bst_length:
            stack.append((left_index_bst, left, parent))

        if right_index_bst < bst_length:
            stack.append((right_index_bst, right, parent))

    return aBST
