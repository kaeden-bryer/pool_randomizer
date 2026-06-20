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
    "Emma & TBD",
    "Duyen & Ian",
    "Jaina & LJ",
    "Benny & Kaylee",
    "Mitch & Grace",
    "Nathan & Teresa",
    "Sarah & Jaden",
    "Ghost",
    "Ghost",
    "Ghost",
    "Ghost",
]

def make_pool(pairs, pool_num):
    print("Pool " + str(pool_num) + ":")
    for i in range(1,6):
        pair_num = random.randint(0, len(pairs) - 1)
        print(pairs[pair_num])
        pairs.pop(pair_num)
    print("")

if __name__ == "__main__":
    for i in range(1,5):
        make_pool(pairs, i)