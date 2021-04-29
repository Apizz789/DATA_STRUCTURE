if __name__ == "__main__":
    inp = int(input("Enter : "))
    stars = 1
    space = (2*inp) - 2

    for _ in range(inp):        #TOP
        for _ in range(stars):
            print("*", end='')
        for _ in range(space):
            print(" ", end='')
        for _ in range(stars):
            print("*", end='')
        stars += 1
        space -= 2
        print()
    
    stars -= 1
    space += 2
    
    for _ in range(inp-1):        #Bottom
        stars -= 1
        space += 2
        for _ in range(stars):
            print("*", end='')
        for _ in range(space):
            print(" ", end='')
        for _ in range(stars):
            print("*", end='')
        print()