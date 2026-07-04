"""
Data Pipeline
"""
import sys # give access to system-level information and command-lines arguments, gives access to Python's system interface tools
import pandas as pd # library for data processing

print("arguments", sys.argv) # list of command-line arguments passed into the script

day = int(sys.argv[1])

df = pd.DataFrame({"id": [1, 2], "name": ["xuxin", "xuyi"]})
print(df.head())
print(f"Running pipeline for day {day}")
# save this data frame to a Parquet file 
# a parquet file is a fast, compressed column-based data format used a lot in data eningeering
df.to_parquet(f"output_day_{day}.parquet") 

'''
Download uv (virtual machine)
download PyArrow in uv
- VM gives a clean, isolated environment
'''


# to read the parquet file 
# read_parquet_df = pd.read_parquet("output_day_12.parquet")
# print(read_parquet_df.head())