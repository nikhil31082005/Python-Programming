letter = '''Dear <|NAME|> ,
Greeting from ABC coding house, I am happy to tell about your selection.
You are selected!
Thanks and regards,
Bill
Date = <|DATE|>
'''
name = input("Enter your name :\n")
date = input("Enter date of selection :\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)