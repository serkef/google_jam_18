from operator import itemgetter

speeds = []

for case in range(int(input(''))):

    horses = []
    my_distance, horse_count = list(map(int, input('').split()))

    for i in range(horse_count):
        horse = {}
        x_pos, horse['speed'] = list(map(int, input('').split()))
        horse['distance'] = my_distance - x_pos
        horses.append(horse)

    # Sort horses based on remaining distance
    horses = sorted(horses, key=itemgetter('distance'), reverse=True)

    # Find each horse's ETA
    for i, horse in enumerate(horses):
        horse['time'] = horse['distance'] / horse['speed']
        horse['time'] = max(horse['time'], horses[i - 1]['time']) if i > 0 else horse['time']

    # My speed is defined by the time of the horse ahead
    speeds.append(my_distance / horses[-1]['time'])

for case, speed in enumerate(speeds):
    print("Case #%s: %s" % (case + 1, speed))

