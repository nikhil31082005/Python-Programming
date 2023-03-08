str = input("Enter a string or name : ")
l = len(str)
count_vowel = 0

for i in range(l):
    if str[i]== 'a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
        count_vowel += 1
print(f"Number of vowel is {count_vowel}")
print(f"Number of consonent is {l-count_vowel}")