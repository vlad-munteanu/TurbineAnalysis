#!/usr/bin/python3
import csv

# Constants
swept_area = 0.15
air_density = 1.2754
air_velocity = 1.75


# This reads the data from the data file
def readData():
    fp = open("data.csv")
    reader = csv.reader(fp)
    data_list = []

    # Skips first line of csv file
    next(reader)
    for line in reader:
        resistance = float(line[0])
        voltage = float(line[1])
        data_list.append((resistance, voltage))
    return data_list

# Electrcial power generated equation
def electricalPower(datalist):
    temp_list = []

    for item in datalist:
        power = (pow(item[1], 2)/(item[0]))
        efficiency = (power/maxTurbinePower()) * 100
        temp_list.append(
            (item[0], item[1], power, maxTurbinePower(), efficiency))
    return temp_list

# Turbine power equation
def maxTurbinePower():
    power = (0.5) * (air_density) * (swept_area) * \
        (pow(air_velocity, 3)) * 0.59
    return power

# Prints output in a table
def printOutput(listToPrint):
    header = ['Resistance (ohms)', 'Voltage (volts)',
              'Power Generated (W)', 'Turbine Power (W)', 'Efficiency']
    print("{}  {:15s}  {:15s}  {:15s}  {:15s}".format(*header))

    for items in listToPrint:
        print("{}          {:15f}      {:15f}    {:15f}  {:15f}".format(*items))


def main():
    printOutput(electricalPower(readData()))

if __name__ == "__main__":
    main()
