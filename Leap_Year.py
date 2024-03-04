def leap_year(year):
    if year %4==0 and year %100!=0 or year %400==0:
        return True
    else:
        return False
days=[31,28,31,30,31,31,30,31,30,31,30,31]
def checking(year,month):

    if year==leap_year(year) and month==2:
        return 29
    else:
        return days[month-1]




year=int(input("enter-"))
month=int(input("enter-"))
result=checking(year,month)
print(result)