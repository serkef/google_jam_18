from collections import Counter

for case in range(int(input(''))):
    nof_customers = int(input(''))
    lollipops = [x for x in range(nof_customers)]
    pref_stats = Counter()

    for _ in range(nof_customers):
        pref_list = list(map(int, input('').split()))
        if pref_list[0] == -1:
            exit(1)
        pref_list.pop(0)  # first is not an actual preference

        # update my stats
        pref_stats.update(pref_list)

        for pref in sorted(pref_list, key=lambda x: pref_stats[x]):
            if pref in lollipops:
                lollipops.remove(pref)
                print(pref)
                break
        else:
            print(-1)
