def cyclic_shift(nums_left, nums_right=[]):
    """
    Алгоритм циклический сдвиг.
    Сдвиг может происходить влево или вправо.
    """
    # Влево
    tmp_left = nums_left[0]
    for k in range(len(nums_left) - 1):
        nums_left[k] = nums_left[k + 1]
    nums_left[len(nums_left) - 1] = tmp_left
    # Вправо
    tmp_right = nums_right[0]
    for k in range(len(nums_right) - 2, -1, -1):
        nums_right[k + 1] = nums_right[k]
    nums_right[0] = tmp_right
    return nums_left



