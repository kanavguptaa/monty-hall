import random

def monty_hall(switch, num_trials):

    win_count = 0

    doors = ["door1", "door2", "door3"]

    for trials in range(num_trials):
        car_door = random.choice(doors) 
        player_door = random.choice(doors)

        available_doors = []
        
        for door in doors:
            if door != car_door and door != player_door: #add door to available door,if door is not equal to car door or player's door
                available_doors.append(door)

        open_door = random.choice(available_doors) #opens a random available door

        if switch == True:
            for door in doors:
                if door != player_door and door != open_door:
                    player_door = door
                    break

        if player_door == car_door:
            win_count += 1

    return (100 * win_count) / num_trials

print('\n')
print(f"probability when switching: {monty_hall(True, 10000)} %")
print(f"probability when not switching: {monty_hall(False, 10000)} %")
print('\n')