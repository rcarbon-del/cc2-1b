movecounter = 0

def toh(n, rod1, rod2, rod3):
    global movecounter
    if n == 0:
        return
    toh(n-1, rod1, rod3, rod2)
    print(f"Move disk {n} from rod {rod1} to rod {rod2}.")
    movecounter += 1
    toh(n-1, rod3, rod2, rod1)

disks = int(input("Enter number of disks: "))
toh(disks, 'A', 'B', 'C')
print(f"Total number of moves: {movecounter}")