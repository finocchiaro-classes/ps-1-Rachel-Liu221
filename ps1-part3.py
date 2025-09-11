def heart_rate(age, goal):
    max_HR = 220 - age
    print("Your maximum heart rate is:", max_HR)

    if goal == "S":
        low = 0.8 * max_HR
        print("Your target heart rate is between", low, "and", max_HR)
    elif goal == "E":
        low = 0.6 * max_HR
        high = 0.8 * max_HR
        print("Your target heart rate is between", low, "and", high)

user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")

heart_rate(user_age, user_goal)

