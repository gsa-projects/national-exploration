import pandas as pd

# read in the csv files
duck1 = pd.read_csv('duck1.csv')
duck1.rename(columns={'x': 'x1', 'y': 'y1'}, inplace=True)
duck2 = pd.read_csv('duck2.csv')
duck2.rename(columns={'x': 'x2', 'y': 'y2'}, inplace=True)

print(duck1.head())
print(duck2.head())

# merge the dataframes on the 'time' column, using the shorter dataframe as the base
if len(duck1) < len(duck2):
    merged = pd.merge(duck1, duck2, on='t')
else:
    merged = pd.merge(duck2, duck1, on='t')

# write the merged dataframe to a new csv file
merged.to_csv('merged_ducks.csv', index=False)