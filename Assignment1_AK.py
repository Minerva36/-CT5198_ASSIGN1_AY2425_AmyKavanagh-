#Amy Kavanagh 24102830 27/January/2025

#Defining the main function to perform the task of gathering
#information on number of customers per business day
def main():
    # Creating an empty list to store the number of customers
    customers = []
    #asking user to input the number of customer from days 1-7
    print("Please enter the number of customers per day:")
    for day in range(1, 8):
        #when a valid integer is input
        while True:
            #the program will ask for a value for the consecutive day
            try:
                count = int(input(f"Day {day}: "))
                #if an invalid (negative integer or string is entered
                #the program will prompt to enter a valid integer
                if count < 0:
                    print("Please enter a positive integer")
                    continue
                customers.append(count)
                break
                #value error ensures the program does not crash when invalid
                #values are entered
            except ValueError:
                #shows the user what to do to get the program to run effectively
                print("Please enter a valid integer")
    #calculates the max number of customers
    max_customers = max(customers)
    #calculates the minimum number of customers
    min_customers = min(customers)
    #calculates the average number of customers
    avg_customers = sum(customers) / len(customers)
    #Prints the calculations from above
    print("\nWeekly customers")
    print(f"Max customers: {max_customers}")
    print(f"Min customers: {min_customers}")
    #calculates to two decimal places
    print(f"Average customers: {avg_customers:.2f}")

#checks if program is running in the main scope
if __name__ == "__main__":
    main()