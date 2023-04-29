import csv
import matplotlib.pyplot as plt

times_v1 = []
times_v2 = []
times_v3 = []
sizes = []

with open('csv files/time_data_qs_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        if row[1] == "1":
            sizes.append(row[0])
            times_v1.append(float(row[2]))

with open('csv files/time_data_qs_inc.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        if row[1] == "2":
            times_v2.append(float(row[2]))


with open('csv files/time_data_qs_dec.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t') # as headers in a .csv file are separated by tabs
    next(reader) # skip the header row
    for row in reader:
        if row[1] == "3":
            times_v3.append(float(row[2]))

plt.plot(sizes, times_v1,label = "First Element")
plt.plot(sizes, times_v2, label = "Random Element")
plt.plot(sizes, times_v3, label = "Median Element")
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Quick Sort Best Case')

plt.legend()
plt.show()