response = "Case #{x}: {y}"
results = []


def figure_ants(weights):
    weights = weights[::-1]
    while True:
        for idx, ant in enumerate(weights):
            if 7 * ant < sum(weights[idx:]):
                # colony not ready yet, send the fat guy home
                weights.remove(max(weights[idx:]))
                break
        else:
            # colony ready
            return len(weights)


for case in range(int(input(''))):
    nof_ants = int(input(''))
    weights = list(map(int, (input('')).split()))

    ant_colony = figure_ants(weights)
    results.append(response.format(x=case + 1, y=ant_colony))

for result in results:
    print(result)
    
