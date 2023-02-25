salary = int(input("Enter your basic salary : "))

if salary <= 10000 :
    gross_salary = salary + (salary*20)/100 + (salary*80)/100
    print(f'Gross salary is {gross_salary}')

elif salary <= 20000 :
    gross_salary = salary + (salary*25)/100 + (salary*90)/100
    print(f'Gross salary is {gross_salary}')

else :
    gross_salary = salary + (salary*30)/100 + (salary*95)/100
    print(f'Gross salary is {gross_salary}')