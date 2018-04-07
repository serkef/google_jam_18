results = []
response = "Case #{x}: {sortable}"


def trouble_solve(l):
    even = sorted(l[::2], reverse=True)
    odd = sorted(l[1::2], reverse=True)

    all_troublesort = []
    for i in range(len(l)):
        if i % 2 == 0:
            all_troublesort.append(even.pop())
        else:
            all_troublesort.append(odd.pop())

    all_timsort = sorted(l)

    for i, (x, y) in enumerate(zip(all_troublesort, all_timsort)):
        if x != y:
            return i
    return 'OK'


for case in range(int(input(''))):
    len_list = int(input(''))
    l = list(map(int, input('').split()))

    results.append(response.format(x=case + 1, sortable=trouble_solve(l)))

for result in results:
    print(result)
