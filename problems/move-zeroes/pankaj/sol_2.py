# Realize that every swap moves zero_start_index forward
def moveZeroes(a):
    n = len(a)
    zero_start_index = -1
    for i in range(n):
        if a[i] == 0 and zero_start_index == -1:
            zero_start_index = i
        if a[i] != 0 and zero_start_index != -1:
            a[i], a[zero_start_index] = a[zero_start_index], a[i]
            zero_start_index += 1
