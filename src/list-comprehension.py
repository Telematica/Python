fil = [x for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) if x % 2 != 0]
fil2 = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 != 0]
fil3 = [x for x in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} if x % 2 != 0]
fil4 = [x for x in range(10) if x % 2 != 0]

print(type(fil), fil, type(fil2), fil2, type(fil3), fil3, type(fil4), fil4)
