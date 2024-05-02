# 3. Working with CSV
# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily
# measurements at Mauna Loa, Hawaii dataset, obtained from here
# (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
#
# Annual average for each year in the dataset.

import csv
co2_total = []
co2_count = []
years_list = []
# # created empty list

with (open("co2-ppm-daily.csv") as co2_csv):
    next(co2_csv)
    for row in csv.reader(co2_csv):
        date = row[0]
        year = int(date.split('-')[0])
        # splitting y-d-m to only get year, saves year as integer
        # https://www.altcademy.com/blog/how-to-use-split-in-python/
        value = float(row[1])
        if year not in years_list:
            years_list.append(year)
            co2_total.append(0)
            co2_count.append(0)
        co2_total[years_list.index(year)] += value
        co2_count[years_list.index(year)] += 1
# # updates sum and count as they go
# increases total by co2 value and increases count by 1

# used index because i ran into an index error. index helps to look for the years to update the running total.
# https://rollbar.com/blog/python-indexerror/ used this to help me.

for i in range(len(years_list)):
    year = years_list[i]
    co2_sum = co2_total[i]
    count = co2_count[i]
    annual_average = None if count == 0 else co2_sum / count
    # makes sure youre not dividing by 0, source=
    # https://stackoverflow.com/questions/72103862/how-can-i-avoid-errors-when-dividing-by-zero-when-using-multiple-lists

    print("Year: " + str(year) + " Annual Average: " + str(annual_average))

# # Minimum, maximum and average for the entire dataset.
#
# Seasonal average if Spring (March, April, May), Summer (June, July, August),
min_value = []
max_value = []
total_value = 0
total_value_count = 0

with open("co2-ppm-daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        value = float(row[1])
        min_value.append(row[1])
        max_value.append(row[1])
        total_value += value
        total_value_count += 1

overall_average = None if total_value_count == 0 else total_value / total_value_count

print('Minimum CO2 Value:', min(min_value))
print('Maximum CO2 Value:', max(max_value))
# min and max find min and max values in the min and max list!
print('Average CO2 Value: ' + str(overall_average))

# source: https://stackoverflow.com/questions/48920014/how-to-extract-the-min-value-and-max-value-from-csv-file-using-python

# Seasonal average if Spring (March, April, May), Summer (June, July, August),
spring_count = 0
spring_co2 = 0
summer_count = 0
summer_co2 = 0
# found in the last problem that storing counts/sums when not using append as a value not a list is better for me

with open("co2-ppm-daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        date = row[0]
        month = int(date.split('-')[1])
        # this splits month- when i split year i used [0] so i used [1] for month (second variable in date string)
        value = float(row[1])
        if 4 <= month <= 6:
            spring_co2 += value
            spring_count += 1
        elif 7 <= month <= 9:
            summer_co2 += value
            summer_count += 1
spring_average = None if spring_count == 0 else spring_co2 / spring_count
summer_average = None if summer_count == 0 else summer_co2 / summer_count

print("Spring Average: ", spring_average)
print("Summer Average: ", summer_average)


# Autumn (September, October, November) and Winter (December, January, February).

autumn_count = 0
autumn_co2 = 0
winter_count = 0
winter_co2 = 0
# found in the last problem that storing avg as a list and count as an integer is easier!

with open("co2-ppm-daily.csv") as co2_csv:
    next(co2_csv)
    for row in csv.reader(co2_csv):
        date = row[0]
        month = int(date.split('-')[1])
        value = float(row[1])
        if 1 <= month <= 3:
            winter_co2 += value
            winter_count += 1
# what i did for my first average thing
        elif 10 <= month <= 12:
            autumn_co2 += value
            autumn_count += 1
autumn_average = None if autumn_count == 0 else autumn_co2 / autumn_count
winter_average = None if winter_count == 0 else winter_co2 / winter_count

print("Autumn Average: ", autumn_average)
print("Winter Average: ", winter_average)
#
# Just a note: I am going by solstice rounding rules here,
# meaning fall is 9-21 to 12-21, so im using 10-12 as the months.
#
# Calculate anomaly for each value in the dataset relative to the mean for the entire time series.

average = float(overall_average)

years_list = []
total_value = []

with (open("co2-ppm-daily.csv") as co2_csv):
    next(co2_csv)
    for row in csv.reader(co2_csv):
        date = row[0]
        year = int(date.split('-')[0])
        value = float(row[1])
        if year not in years_list:
                years_list.append(year)
                total_value.append(value)
        anomaly_list = [value - average for value in total_value]
for i in range(len(years_list)):
    year = years_list[i]
    anomaly = anomaly_list[i]
    print("The anomaly in " + str(year) + " was " + str(anomaly))

