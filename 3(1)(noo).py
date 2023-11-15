for n in range(2, 10, 4):
    for i in range(n, n + 4):
        print(f"    {i}단   ", end = "\t")
    print ()
    for i in range(1, 10):
        for j in range(n, n + 4):
            print(f"{j} * {i} = {j * i : 2d}", end = "\t")
        print()
    print()