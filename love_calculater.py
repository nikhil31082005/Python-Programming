name1 = input("Enter your name : ")
name2 = input("Enter his/her name : ")

combined_name = name1 + name2
lower_case_name = combined_name.lower()

t = lower_case_name.count('t')
r = lower_case_name.count('r')
u = lower_case_name.count('u')
e = lower_case_name.count('e')

l = lower_case_name.count('l')
o = lower_case_name.count('o')
v = lower_case_name.count('v')
e = lower_case_name.count('e')

true = t+r+u+e
love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score<10 or love_score>90:
    print(f'Your love score is {love_score} and you go together like coke and mentos.')

elif love_score >= 40 and love_score <=50:
    print(f'Your love score is{love_score} and you are alright together.')

else:
    print(f'Your love score is {love_score}')
