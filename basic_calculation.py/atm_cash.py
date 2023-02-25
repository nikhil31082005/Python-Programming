amount = int(input("Enter the amount :\n"))

twok = amount // 2000
amount = amount % 2000

fiveh = amount // 500
amount = amount % 500

twoh = amount // 200
amount = amount % 200

oneh = amount // 100
amount = amount % 100

fifty = amount // 50
amount = amount % 50

twenty = amount // 20
amount = amount % 20

ten = amount // 10
amount = amount % 10

five = amount // 5
amount = amount % 5

two = amount // 2
amount = amount % 2

one = amount // 1

print("nNo of notes of two thousand",twok)
print("nNo of notes of five hundred",fiveh)
print("nNo of notes of two hundred",twoh)
print("nNo of notes of one hundred",oneh)
print("nNo of notes of fifty",fifty)
print("nNo of notes of twenty",twenty)
print("nNo of notes of ten",ten)
print("nNo of notes of five",five)
print("nNo of notes of two",two)
print("nNo of notes of one",one)