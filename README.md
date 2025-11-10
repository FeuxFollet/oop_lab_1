# Cities Data Filter and Aggregator

A Python program that works with Cities.csv file, which store datas for different countries around the world to allow filtering and aggreating data.

## File Structure

- `Cities.csv`: Contains all the data for different countries around the world.
- `data_processing.py`: Contains all the Python code which is used to filter and aggregate the data.

## DataLoader Class

Loads csv file and turn it into a table which is a list of dictionaries.

### Attributes
- `base_path` (Path): Use to locate the csv file.

### Methods
- `load_csv(self, filename)`: Load a csv file and return the content as a list of dictionaries

## Table Class

Store the data loaded from dataloader and contains different methods to filter and aggregate the data.

### Attributes
- `name` (str): Name of the table.
- `table` (list): Data of all the cities.

### Methods
- `aggregate(self, func, key)` : Applies a function (`func`) to all list of values under a given column (`key`). 
- `filter(self, condition)` : Filters the data given the condition.

##  How the program works

1. Load the data from Cities.csv using DataLoader.
2. Store the data in Table object.
3. Filter and aggregate the data using the methods according to each condition.