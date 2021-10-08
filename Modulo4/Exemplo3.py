def is_year_leap(year):
    print('Enter a year:', year)
    return(year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(year, month):
    print('Enter a month:', year, month)
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    if month in month_31:
        return 31
    if month == 2:
        if is_year_leap(year):
            return 29
        return 28
    return 30

def day_of_year(year, month, day):
    y = year
    m = month
    d = day
    A = B = C = D = E = 0
    if m < 3:
        y = y - 1
        m = m + 12
    if y >= 1582:
        A = y // 100
        B = m // 4
        C = 2 - A + B     
    if y < 1582:
        C = 0
        D = int(365.25 * (y + 4716))
        E = int(30.6001 * (m + 1))
    print(y, m, d, A, B, C, D, E)
    return D + E + d + C - 1524.5

print(day_of_year(2021, 10, 7))
