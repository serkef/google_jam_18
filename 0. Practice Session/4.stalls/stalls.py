results = []
response = "Case #{x}: {y} {z}"


def stall_allocator(stalls):
    occupied = [0, stalls + 1]
    while len(occupied) - 2 < stalls:
        alloc_stall = -1
        min_cost = -1
        max_cost = -1
        allocated = []

        for left, right in zip(occupied, occupied[1:]):
            if left + 1 < right:
                new_stall = (left + right) // 2
                new_min_cost = min(new_stall - left - 1, right - new_stall - 1)
                new_max_cost = max(new_stall - left - 1, right - new_stall - 1)
                if new_min_cost > min_cost or (new_min_cost == min_cost and new_max_cost > max_cost):
                    min_cost = new_min_cost
                    max_cost = new_max_cost
                    alloc_stall = new_stall
                    allocated.append(alloc_stall)

        occupied.extend(allocated)

        yield (alloc_stall, min_cost, max_cost)


for case in range(int(input(''))):
    stalls, people_waiting = list(map(int, input('').split()))
    stall_cpu = stall_allocator(stalls)

    for p in range(people_waiting):
        stall, min_d, max_d = next(stall_cpu)

    results.append(response.format(x=case + 1, y=max_d, z=min_d))

for result in results:
    print(result)
