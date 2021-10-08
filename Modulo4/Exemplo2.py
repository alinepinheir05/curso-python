def is_year_leap(year):
    return(year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(year, month):
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    if month in month_31:
        return 31
    if month == 2:
        if is_year_leap(year):
            return 29
        return 28
    return 30

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")