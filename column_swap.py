# Problem
# In the attached "machine-readable-business-employment-data-mar-2023-quarter.csv" file
# swap "Data_value" column position with "Subject" column position.

# Solution
def run(csv_file_name, data_value_col, subject_col):
    # Open a new file for writing
    csv_file = open(csv_file_name, 'r')
    new_csv_file = open('swapped_' + csv_file_name, 'w')
    # Loop through each row in the csv_file
    for row in csv_file:
        # Split the row into a list using ',' as the delimiter
        row = row.split(',')

        # Swap values between start_column and end_column
        row[data_value_col], row[subject_col] = row[subject_col], row[data_value_col]

        # Write the modified row to the new file
        new_csv_file.write(','.join(row))

    # Close used files
    new_csv_file.close()
    csv_file.close()
    return True


assert run('machine-readable-business-employment-data-mar-2023-quarter.csv', 2, 7)
print("Test Case Passed")
