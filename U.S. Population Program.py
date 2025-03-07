def main():
    data = []  # List to store the year, state, and population data


    while True:
        year = input("Enter the year (or type 'done' to stop): ")
        if year.lower() == 'done':
            break
        state = input("Enter the name of the state: ")
        population = input("Enter the population of the state: ")


        try:
            year = int(year)
            population = int(population)


            data.append([year, state, population])
        except ValueError:
            print("Invalid input. Please enter numerical values for year and population.")


    search_year = int(input("Enter the year you want to search for: "))


    total_population = 0
    for entry in data:
        if entry[0] == search_year:
            total_population += entry[2]


    if total_population > 0:
        print(f"The total population for the year {search_year} is {total_population}.")
    else:
        print(f"No data found for the year {search_year}.")


main()