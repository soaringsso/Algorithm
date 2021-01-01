def quick_sort (A, first, last):
    global Qc, Qs
    if first >= last : 
        return
    left, right = first + 1 , last
    pivot = A[first]
    while left <= right :
        while left <= last and A[left] < pivot :
            Qc += 1
            left += 1
        while right > first and A[right] > pivot :
            Qc += 1
            right -= 1
        if left <= right : # swap A[left] and A[right]
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1
            right -= 1
    # place pivot at the right place
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort (A, first, right- 1)
    quick_sort (A, right+1, last)