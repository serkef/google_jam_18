results = []
response = "Case #{x}: {sortable}"


def trouble_solve(l):
    even = sorted(l[::2])
    odd = sorted(l[1::2])

    all_troublesort = []
    for i in range(len(l)):
        if i % 2 == 0:
            all_troublesort.append(even.pop(0))
        else:
            all_troublesort.append(odd.pop(0))

    for i in range(len(all_troublesort)-1):
        if all_troublesort[i] > all_troublesort[i+1]:
            return i

    return 'OK'


for case in range(int(input(''))):
    len_list = int(input(''))
    l = list(map(int, input('').split()))

    results.append(response.format(x=case + 1, sortable=trouble_solve(l)))

for result in results:
    print(result)
