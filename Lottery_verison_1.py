import random

MM_numbers = [num for num in range(1,71)]
MB_nums = [num for num in range(1,26)]
PB_numbers = [num for num in range(1,70)]
PB_nums = [num for num in range(1,27)]
NDR_MM = 888
NDR_PB = 888
random_MM = random.randrange(NDR_MM)
random_PB = random.randrange(NDR_PB) 

# def lottery_picker():
#     mega_numbers = random.sample(MM_numbers, k=5)
#     MB_number = random.choice(MB_nums)
#     power_numbers = random.sample(PB_numbers, k=5)
#     PB_number = random.choice(PB_nums)
#     print(f"""Next time you play the lottery use these numbers
#     \nMega Millions: {mega_numbers} with a Mega Ball number of {MB_number}
#     \nPowerball: {power_numbers} with a Power Ball number of {PB_number}
#     \n - - - - - - - - """)
   
def MM_picker():
    print("Next time you play Mega Millions use these numbers")
    for i in range(5):
        for k in range(NDR_MM):
            mega_numbers = random.sample(MM_numbers, k=5)
            MB_number = random.choice(MB_nums)
            if k == random_MM:
                print(f"""Mega Millions: {mega_numbers} with a Mega Ball number of {MB_number}
                \n - - - - - - - - """)

def PB_picker():
    print("Next time you play Powerball use these numbers")
    for i in range(5):
        for k in range(NDR_PB):
            power_numbers = random.sample(PB_numbers, k=5)
            PB_number = random.choice(PB_nums)
            if k == random_PB:
                print(f"""\nPowerball: {power_numbers} with a Power Ball number of {PB_number}
                \n - - - - - - - - """)

#MM_picker()
PB_picker()                