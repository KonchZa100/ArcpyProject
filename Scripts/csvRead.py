# This script reads a GPS track in CSV format and
#  prints a list of coordinate pairs
import csv

# Set up input and output variables for the script
gpsTrack = open(r'F:\Demidov\PythEveryone\PyCharmProject\Lesson3\gps_track.txt', "r")

# Set up CSV reader and process the header
csvReader = csv.reader(gpsTrack)
header = csvReader.next()
latIndex = header.index("lat")
lonIndex = header.index("long")

# Make an empty list
coordList = []

# Loop through the lines in the file and get each coordinate
for row in csvReader:
    lat = float(row[latIndex])
    lon = float(row[lonIndex])
    coordList.append([lat,lon])

# Print the coordinate list
print coordList
