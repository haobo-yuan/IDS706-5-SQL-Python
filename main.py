import lib

# Load data
lib.my_load(nrows=3)
print("Data loaded into the database.")

# Create a new record
lib.my_create(record=('2021-10-01', 100, 110, 90, 105, 1000000, 'Imaginary AAPL'))
print("New record created.")

# Read the records
results = lib.my_read(name='Imaginary AAPL')
print("Read records:")
for row in results:
    print(row)

# Update the record
lib.my_update(name='Imaginary AAPL', new_close=200)
print("Record updated.")

# Read the records after update
results = lib.my_read(name='Imaginary AAPL')
print("Read records after update:")
for row in results:
    print(row)

# Delete the record
lib.my_delete(name='Imaginary AAPL')
print("Record deleted.")

# Read the records after deletion
results = lib.my_read(name='Imaginary AAPL')
print("Read records after deletion:")
print(results)
