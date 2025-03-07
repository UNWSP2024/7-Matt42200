def main():
    rainfall = []
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    
    for i in range(12):
        while True:
            try:
                rainfall_amount = float(input(f"Enter the total rainfall for {months[i]} (in inches): "))
                if rainfall_amount < 0:
                    print("Rainfall cannot be negative. Please enter a valid amount.")
                else:
                    rainfall.append(rainfall_amount)
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for rainfall.")
    
    total_rainfall = sum(rainfall)
    
    average_rainfall = total_rainfall / 12
    
    highest_rainfall = max(rainfall)
    lowest_rainfall = min(rainfall)
    
    highest_month = months[rainfall.index(highest_rainfall)]
    lowest_month = months[rainfall.index(lowest_rainfall)]
    
    print(f"\nTotal rainfall for the year: {total_rainfall} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with the highest rainfall: {highest_month} ({highest_rainfall} inches)")
    print(f"Month with the lowest rainfall: {lowest_month} ({lowest_rainfall} inches)")


main()