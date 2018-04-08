s = 'S'
c = 'C'
results = []
response = "Case #{x}: {swaps}"


def damage(attack):
    power = 1
    damage = 0
    shots = 0
    for instruction in attack:
        if instruction == c:
            power *= 2
        else:
            shots += 1
            damage += power
    return shots, damage


def defense(attack, shield_power):
    attack = [x for x in attack]
    base_damage, max_damage = damage(attack)
    damage_diff = max_damage - shield_power

    if base_damage > shield_power:
        return 'IMPOSSIBLE'

    swaps = 0
    while damage_diff > 0:
        # find last shoot
        i = attack[::-1].index(s)
        i = len(attack) - i -1
        # find last charge prior to last shoot
        j = attack[i::-1].index(c)
        j = i - j
        # in case of multiple shoots after the last charge, take the first
        i = j + 1
        # damage of a shot is 2^number_of_prior_charges
        damage_gain = 2 ** attack[:j].count(c)
        # swap
        attack[i], attack[j] = c, s
        damage_diff -= damage_gain
        swaps += 1

    return swaps


for case in range(int(input(''))):
    shield, attack = input('').split()

    results.append(response.format(x=case + 1, swaps=defense(attack, int(shield))))

for result in results:
    print(result)
