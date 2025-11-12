# Data tables Filter and Joiner

A Python program that works with Cities.csv and Countries.csv file, which store datas for different countries around the world, and allows filtering and joining of these data tables.

## File Structure

- `Cities.csv`: Contains latitude, longtidude, and temperature data from cities all over the world.
- `Countries.csv` : Contains population, coastline existence, and location in EU of different countries.
- `data_processing.py`: Contains all the Python code which is used to filter and aggregate the data.

## DataLoader Class

Loads csv file and turn it into a table which is a list of dictionaries.

### Attributes
- `base_path` (Path): Use to locate the csv file.

### Methods
- `load_csv(self, filename)`: Load a csv file and return the content as a list of dictionaries

## DB Class

A Database that essentially stores all the tables in a list

### Attributes
- `database` (list): A database list that stores all the tables.

### Methods
- `insert(self, table_obj)` : Add a `table_obj` into the database.
- `search(self, search_name)` : Search a specific table inside the databse by it's name and return that object.

## Table Class

Store the data loaded from dataloader and contains different methods to filter and aggregate the data.

### Attributes
- `name` (str): Name of the table.
- `table` (list): Data of all the cities.

### Methods
- `aggregate(self, func, key)` : Applies a function (`func`) to all list of values under a given column (`key`). 
- `filter(self, condition)` : Filters the data given the condition.
- `join(self, table_to_join, pivot)` : Join the self table with another one using `pivot` as a reference for what data to match. Returns the joined_table.

##  How the program works

1. Load the data from Cities.csv and Countries.csv using DataLoader.
2. Store each table in the DB object.
3. Filter and join the data using the methods according to each condition.

##  Running the program

To run the program, execute `data_processing.py`:

```bash
python data_processing.py