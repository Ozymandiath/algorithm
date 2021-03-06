def cyclic_shift(nums_left, nums_right=[1, 2, 3]):
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


def insert_sort(nums):
    """
    Сортировка списка nums вставками.
    O(n^2).
    """
    for top in range(1, len(nums)):
        k = top
        while k > 0 and nums[k - 1] > nums[k]:
            nums[k], nums[k - 1] = nums[k - 1], nums[k]
            k -= 1


def choise_sort(nums):
    """
    Сортировка списка nums выбором.
    O(n^2).
    """
    for pos in range(0, len(nums) - 1):
        for k in range(pos + 1, len(nums)):
            if nums[k] < nums[pos]:
                nums[k], nums[pos] = nums[pos], nums[k]


def bubble_sort(nums):
    """
    Сортировка списка nums методом пузырька
    O(n^2).
    """
    for bypass in range(1, len(nums)):
        for k in range(0, len(nums) - bypass):
            if nums[k] > nums[k + 1]:
                nums[k], nums[k + 1] = nums[k + 1], nums[k]


def binSearch(nums, target, leftBias):
    """
    Бинарный поиск левой и правой границы
    :param leftBias: True - левая границв, False - правая граница
    :return: возвращает id одной из границы
    O(log n)
    """
    l, r = 0, len(nums) - 1
    i = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:  # if nums[m] == target
            i = m
            if leftBias:  # if I'm searching from left-side
                r = m - 1
            else:  # if I'm searching from right-side
                l = m + 1
    return i


def rle(stroka):
    """
    Алгоритм сжатия одинаковых символов в последовательности
    """

    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = stroka[0]
    lastpos = 0
    ans = []
    for i in range(len(stroka)):
        if stroka[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastsym = stroka[i]
            lastpos = i
    ans.append(pack(lastsym, len(stroka) - lastpos))
    return "".join(ans)


def countsort(nums):
    """
    Сортировка подсчетом
    O(N+K)
    """
    minval = min(nums)
    maxval = max(nums)
    k = (maxval - minval + 1)
    count = [0] * k
    for now in nums:
        count[now - minval] += 1
    nowpos = 0
    for i in range(0, k):
        for val in range(count[i]):
            nums[nowpos] = i + minval
            nowpos += 1


