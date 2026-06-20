import random

pairs = [
    "Kaeden & Colleen",
    "Moe & Samantha",
    "Pedro & Sunshine",
    "Joseph & Skylar",
    "Hailey & Hatch",
    "Joanie & Mounir",
    "Rick & Alexis",
    "Duke & Allie",
    "Jake & Ellie",
    "Emily & Andrew",
    "SK & Wren",
    "Trevor & Aaliyah",
    "Delayne & Gavin Roberts",
    "Kadin & Felicia",
    "Gavin Barnard & Delanie",
    "Michael & Anya",
    "Jamie & Harold",
    "Aude & Ashley",
    "Kristin & Connor",
    "Emma & AJ",
    "Duyen & Ian",
    "Jaina & LJ",
    "Benny & Kaylee",
    "Mitch & Grace",
    "Nathan & Teresa",
    "Sarah & Jaden",
]

def make_pools(pairs, pool_count, ghosts):

    pools = [[] for _ in range(pool_count)]

    i = 0
    while pairs:
        if ghosts > 0:
            pools[i].append("Ghost")
            ghosts -= 1
        else:
            rand_num = random.randint(0, len(pairs) - 1)
            pools[i].append(pairs[rand_num])
            pairs.pop(rand_num)

        i = (i+1) % pool_count

    return pools

if __name__ == "__main__":
    pool_count = 5
    pool_size = 6

    ghosts = pool_count * pool_size - len(pairs) # number of ghosts needed to make even pools
    
    pools = make_pools(pairs, pool_count, ghosts)

    for i, pool in enumerate(pools):
        print("Pool " + str(i + 1) + ":")
        for pair in pool:
            print(pair)
        print()