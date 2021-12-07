with open('inputs/1.txt') as file:
    arr = [int(num) for num in file.read().strip().split('\n')]
    # print(arr)
    c = 0
    for idx in range(1, len(arr)):
        if arr[idx] > arr[idx - 1]:
            c += 1

    c2 = 0
    cur_sum = sum(arr[:3])
    for idx in range(3, len(arr)):
        nsum = cur_sum - arr[idx - 3] + arr[idx]
        # print(cur_sum)
        if nsum > cur_sum:
            c2 += 1
        cur_sum = nsum
    print(f'Ans 2: {c2}')
    