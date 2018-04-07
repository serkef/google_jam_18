s = 'S'
c = 'C'
results = []
response = "Case #{x}: {swaps}"


def damage(attack):
    power = 1
    damage = 0
    for instruction in attack:
        if instruction == c:
            power *= 2
        else:
            damage += power
    return damage


def defense(attack, shield_power):
    attack = [x for x in attack]
    base_damage = attack.count(s)
    max_damage = damage(attack)
    damage_diff = max_damage - shield_power

    if base_damage > shield_power:
        return 'IMPOSSIBLE'

    swaps = 0
    while damage_diff > 0:
        i = attack.index(c)
        j = attack.index(s, i)
        i = j - 1
        # damage of a shot is 2^number_of_prior_charges
        damage_gain = 2 ** attack[:i].count(c)
        attack[i], attack[j] = s, c
        damage_diff -= damage_gain
        swaps += 1

    return swaps


for case in range(int(input(''))):
    shield, attack = input('').split()

    results.append(response.format(x=case + 1, swaps=defense(attack, int(shield))))

for result in results:
    print(result)
