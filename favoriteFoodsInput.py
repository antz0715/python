def collect_favorite_foods():
    # Get the number of favorite foods to enter
    while True:
        try:
            num_foods = int(input("How many favorite foods do you have? "))
            if num_foods < 1:
                print("Please enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # List to store the favorite foods
    favorite_foods = []

    # Collect the names of the favorite foods
    for i in range(num_foods):
        food = input(f"Enter favorite food {i+1}: ")
        favorite_foods.append(food)

    # Print the favorite foods
    print("Your favorite foods are:")
    for food in favorite_foods:
        print(food)

collect_favorite_foods()  