# Changes made:
  #Instructions on how to use High's Low's, and Exit
  # Allows the user to select what they want to see (High, Low or Exit)
  # User sees a plot displayed with High's or Low's Temp
  # Program loops until user selects exit
  # WHen exit is used an eit message is displayed
  # Added sys

import csv
import sys #Imported sys to help with a clean exit
from datetime import datetime
from matplotlib import pyplot as plt

# Load the CSV
filename = 'sitka_weather_2018_simple.csv'

dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        # Correct date format: 1/1/2018 (Corrected date format from Y/M/D to M/D/Y)
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        dates.append(current_date)

        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

def show_menu():
    print("\nShow Temperature - enter '1' for High's or '2' for Low's. Enter '3' to exit & quit")

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        # Plot highs
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=18)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=10)
        plt.show()

    elif choice == "2":
        # Plot lows
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=18)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == "3":
        print("Exiting program. Goodbye.")
        sys.exit()

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")