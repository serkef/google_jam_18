import string
from collections import Counter

t = int(input(''))
plans = []

for case in range(t):
    parties = int(input(''))
    plan = []

    senates = (int(n) * string.ascii_uppercase[i] for i, n in enumerate(input('').split()))
    senates_dict = Counter(''.join(senates))

    # STEP 1
    # make 2 top parties, have the same number of representatives by removing people from the top party
    first = senates_dict.most_common(2)[0][0]
    second = senates_dict.most_common(2)[1][0]
    while senates_dict[first] - senates_dict[second] > 0:
        reduce = 1 if senates_dict[first] - senates_dict[second] == 1 else 2
        plan.append(reduce * first)
        senates_dict[first] -= reduce

    # STEP 2
    # while more than 2 parties, remove 2 people from the smallest party (or 1 if only 1 left)
    while len(senates_dict.keys()) > 2:
        last = senates_dict.most_common(3)[-1][0]
        while senates_dict[last] > 0:
            reduce = 1 if senates_dict[last] == 1 else 2
            plan.append(reduce * last)
            senates_dict[last] -= reduce
        del senates_dict[last]

    # STEP 3
    # remove people from top 2 parties, 2 from each, 2 at a time
    first = list(senates_dict.keys())[0]
    second = list(senates_dict.keys())[1]
    for i in range(senates_dict[first]):
        senates_dict[first] -= 1
        senates_dict[second] -= 1
        plan.append(''.join([first, second]))

    plans.append(plan)

for case, plan in enumerate(plans):
    print("Case #%s: %s" % (case + 1, ' '.join(plan)))

