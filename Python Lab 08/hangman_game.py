import random as r

while True:
    ls = ['country','fruit','subject','currency','animal','vegetable','bird']

    opt = r.choice(ls)      # Randomly select the element from ls

    country = ['india','china','brazil','nepal','bhutan','russia','britain','france','germany','canada','africa','australia',\
               'afghanistan','japan','chile','denmark']
    
    fruit = ['banana','papaya','mango','guava','orange','apple','grapes','watermelon','pear','cherry','strawberry','pomegranate']

    subject = ['mathematics','python','chemistry','physics','electronics','electrical','mechanical','biology','social',\
               'drawing','english','hindi']
    
    currency = ['rupee','dollar','euro','rubal','yen','dinar','pound']

    animal = ['dog','cat','bear','camel','donkey','rabbit','zebra','deer','squirrel','fox','pig','horse','lion','tiger',\
              'elephant','giraffe','cow','goat']
    
    vegetable = ['onion','potato','tomato','garlic','ginger','cabbage','cauliflower','brinjal','carrot','peas','radish',\
                 'bottleguard','bitterguard','capsicum','pumkin']
    
    bird = ['parrot','crow','sparrow','hen','swan','peacock','eagle','pigeon','owl','duck','bat','crane','dove']


    choose = r.choice(eval(opt))        # Randomly select the element from the opt
    ls = []
    m = 1       # to find the missed character
    d = 0       # to find the correct lettters
    n = len(choose)         # length of the random word
    k = ''          # for join the ls
    underscore = ['_']*n        # filling correct word enter by user by replacing the underscore('_')
    while True:
        
        if k == choose:       # condition check if random element is equal to k
            print(f"You got it.The word is {choose}.")
            break
        s = input(f"Please guess a character on the basis of {opt} name : ")

        if m == 1:
            if s not in choose:
                ls.append(s)
                print('''
                 +---+
                     |
                     |
                     |
                    ===''')
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                m += 1
            else:
                for i in range(n):
                    if choose[i] == s:
                        underscore[i] = s
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                d += 1

        elif m == 2:
            if s not in choose:
                ls.append(s)
                print('''
                 +---+
                 O   |
                     |
                     |
                    ===''')
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                m += 1
            else:
                for i in range(n):
                    if choose[i] == s:
                        underscore[i] = s
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                d += 1


        elif m == 3:
            if s not in choose:
                ls.append(s)
                print('''
                 +---+
                 O   |
                /    |
                     |
                    ===''')
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                m += 1
            else:
                for i in range(n):
                    if choose[i] == s:
                        underscore[i] = s
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                d += 1

        elif m == 4:
            if s not in choose:
                ls.append(s)
                print('''
                 +---+
                 O   |
                /|   |
                     |
                    ===''')
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                m += 1
            else:
                for i in range(n):
                    if choose[i] == s:
                        underscore[i] = s
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                d += 1

        elif m == 5:
            if s not in choose:
                ls.append(s)
                print('''
                 +---+
                 O   |
                /|\  |
                     |
                    ===''')
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                m += 1
            else:
                for i in range(n):
                    if choose[i] == s:
                        underscore[i] = s
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                d += 1

        elif m == 6:
            if s not in choose:
                ls.append(s)
                print('''
                 +---+
                 O   |
                /|\  |
                /    |
                    ===''')
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                m += 1
            else:
                for i in range(n):
                    if choose[i] == s:
                        underscore[i] = s
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                d += 1

        elif m == 7:
            if s not in choose:
                ls.append(s)
                print('''
                 +---+
                 O   |
                /|\  |
                / \  |
                    ===''')
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                m += 1
            else:
                for i in range(n):
                    if choose[i] == s:
                        underscore[i] = s
                print('Missed letters :',end=' ')
                k = ' '.join(ls)
                print(k)
                print(''.join(underscore))
                d += 1
        

        else:
            print("You have run out of guesses!")
            print(f'After {m-1} missed guesses and {d} correct guesses, the word was "{choose}"')
            break

        

    out = input("Would you like to play again? (y)es or (n)o : ")
    out = out.lower()
    if out == 'yes':
        continue
    else:
        break

print("Thank you for playing.")