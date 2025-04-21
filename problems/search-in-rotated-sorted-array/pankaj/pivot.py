a = [3, 5, 1]
n = len(a)
def getPivot():            
    l, u = 0, n - 1
    while l < u:
        if a[l] < a[u]:
            print(f'a[{l}] < a[{u}]: returning {l}')
            return l
        # l = l + 1
        m = int(l + (u - l) / 2)
        print(f'checking a[m = {m}] with a[l = {l}]')
        # Case of a[l] = a[m] was ignored earlier.
        if a[l] <= a[m]:
            print(f'a[m = {m}] > a[l = {l}], setting l = {m + 1}')
            # pivot is to the right of m
            l = m + 1
            print(f'{l}, {u} (pivot was to right of {m})')
        else:
            # Note sometimes m can be same as l also
            u = m
            print(f'{l}, {u} (pivot was to left of {m})')
        
    return l

k = getPivot()
print(f'pivot is {k}')