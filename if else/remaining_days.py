day = int(input("Enter the day no : \n"))
month = int(input("Enter the month no :\n"))
year = int(input("Enter the year :\n"))

if not(year % 400 == 0 or year % 4 == 0 and year % 100 != 0) :
    if month == 1 :
        remaining_days = (31-day)+28+31+30+31+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 2 :
        remaining_days = (28-day)+31+30+31+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 3 :
        remaining_days = (31-day)+30+31+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 4 :
        remaining_days = (30-day)+31+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 5 :
        remaining_days = (31-day)+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 6 :
        remaining_days = (31-day)+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 7 :
        remaining_days = (31-day)+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 8 :
        remaining_days = (31-day)+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 9 :
        remaining_days = (30-day)+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 10 :
        remaining_days = (31-day)+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month ==11 :
        remaining_days = (30-day)+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 12 :
        remaining_days = (31-day)
        print(f"Remining days in this year is {remaining_days}")

    else :
        print("Enter valid month number .")

else :
    if month == 1 :
        remaining_days = (31-day)+29+31+30+31+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 2 :
        remaining_days = (29-day)+31+30+31+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 3 :
        remaining_days = (31-day)+30+31+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 4 :
        remaining_days = (30-day)+31+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 5 :
        remaining_days = (31-day)+30+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 6 :
        remaining_days = (31-day)+31+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 7 :
        remaining_days = (31-day)+31+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 8 :
        remaining_days = (31-day)+30+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 9 :
        remaining_days = (30-day)+31+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 10 :
        remaining_days = (31-day)+30+31
        print(f"Remining days in this year is {remaining_days}")

    elif month ==11 :
        remaining_days = (30-day)+31
        print(f"Remining days in this year is {remaining_days}")

    elif month == 12 :
        remaining_days = (31-day)
        print(f"Remining days in this year is {remaining_days}")

    else :
        print("Enter valid month number .")