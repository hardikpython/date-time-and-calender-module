import calendar

# Print the names of all the months
for month in calendar.month_name:
    if month:  # This skips the empty string at index 0
        print(month)
