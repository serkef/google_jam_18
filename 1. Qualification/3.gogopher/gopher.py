def gopher_api(req):
    print(req)
    res = input('')
    i, j = map(int, res.split())
    if i == j == 0:
        raise StopIteration
    elif i == j == -1:
        print("req:{req}\tres:{res}. Fuckedup.".format(req=req, res=res))
        raise ValueError
    else:
        return (int(i), int(j))


for case in range(int(input(''))):
    # Will go to the min area (higher or eq to input)
    # that can be formed by triplets (%3==0)
    area = int(input(''))
    area = max(area, 9)
    if area % 3 == 1:
        area += 2
    elif area % 3 == 2:
        area += 1

    marked = [[False, False, False], [False, False, False], [False, False, False]]
    current_row = 2
    current_column = 2  # constant
    column = 1
    while True:
        if all(marked[0]):
            current_row += 1
            marked = [marked[1], marked[2], [False, False, False]]
        try:
            i, j = gopher_api("{} {}".format(current_row, current_column))
            marked[i - current_row + 1][j - 1] = True
        except StopIteration:
            break
        except Exception:
            raise
