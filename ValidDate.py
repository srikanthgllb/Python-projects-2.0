# date = (input("Enter date in dd/mm/year format"))
# date = date.replace("/", "")
# dd = int(date[:2])
# mm = int(date[2:4])
# yyyy = int(date[4:])

dd=int(input("Enter date"))
mm=int(input("Enter month"))
yyyy=int(input("Enter year"))
if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    max_day = 31
elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    max_day = 30
elif yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 400 == 0:
    max_day = 29
else:
    max_day = 28
if mm < 1 or mm > 12:
    print("Entered date is invalid")
    print("Check the range of month")
elif dd < 1 or dd > max_day:
    print("Entered date is Invalid ")
    print("Check the range of date")
else:
    print("Entered date is valid")
