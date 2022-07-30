import pandas as pd
url = 'https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_16/sitka_weather_07-2014.csv'
df = pd.read_csv(url, index_col = 0, parse_dates=[0])


#Base import from CSV 
import csv
filename = 'csvfolder/sitka_weather_07-2014.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  print(header_row)


# Pandas can handle csv files better (much like readxl in R), because it imports it 
# as a dataframe, tihs allows you to manipulate the frame better/easier than base. 

# For the purposes of this exercise we will continue in base CSV import

with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  for index, column_header in enumerate(header_row):
    print(index, column_header)
