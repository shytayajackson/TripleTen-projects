
# TripleTen Guided Case Study: Basic Python

# Dataset
console_data = [
    ['NES', 'Nintendo', 1985, 1995, 179.0, 61910000],
    ['Game Boy', 'Nintendo', 1989, 2003, 89.99, 118690000],
    ['SNES', 'Nintendo', 1990, 2003, 199.0, 49100000],
    ['Virtual Boy', 'Nintendo', 1995, 1996, 179.95, 770000],
    ['Game Boy Advance', 'Nintendo', 2001, 2010, 99.99, 81510000],
    ['Atari 2600', 'Atari', 1977, 1992, 199.0, 30000000],
    ['Sega Genesis', 'Sega', 1988, 1997, 189.0, 30750000],
    ['Game Gear', 'Sega', 1990, 1997, 149.99, 10620000],
    ['Sega CD', 'Sega', 1991, 1996, 299.0, 2240000],
    ['3DO', 'The 3DO Company', 1993, 1996, 699.99, 2000000],
    ['PlayStation', 'Sony Electronics', 1994, 2006, 299.0, 102490000],
    ['PlayStation 2', 'Sony Electronics', 2000, 2013, 299.0, 155000000]
]

# Task 1: Display all rows in the dataset
print("All Console Data:")
for i in range(len(console_data)):
    print(console_data[i])

# Task 2: Retrieve specific console data
print(f"Sega CD Data: {console_data[8]}")
print(f"Game Boy Units Sold: {console_data[1][5]}")

# Task 3: Total units sold for all consoles
total_sold = 0
for item in console_data:
    total_sold += item[-1]
print(f"Total Units Sold: {total_sold}")

# Task 4: Total units sold for Nintendo consoles
nintendo_sold = 0
for item in console_data:
    if item[1] == 'Nintendo':
        nintendo_sold += item[-1]
print(f"Total Nintendo Units Sold: {nintendo_sold}")

# Task 5: Total units sold for Sega consoles and PlayStation (before 1995)
early_units_sold = 0
for item in console_data:
    if item[0] == 'PlayStation':
        early_units_sold += item[-1]
    elif item[1] == 'Sega' and item[2] < 1995:
        early_units_sold += item[-1]
print(f"Early Sega + PlayStation Units Sold: {early_units_sold}")
