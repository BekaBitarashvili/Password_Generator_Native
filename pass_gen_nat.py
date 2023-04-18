import random

pass_length = int(input("შეიყვანეთ პაროლის სიგრძე: "))
pass_lower = input("პაროლში დაბალი ასოების გამოყენება: ")
pass_upper = input("პაროლში მაღალი ასოების გამოყენება: ")
pass_nums = input("პაროლში რიცხვების გამოყენება: ")

upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
integers = "0123456789"
pass_data = ""
for _ in range(pass_length):
    if pass_lower == "ki" and len(pass_data) < pass_length:
        pass_data += random.choice(lower_alphabet)
    if pass_upper == "ki" and len(pass_data) < pass_length:
        pass_data += random.choice(upper_alphabet)
    if pass_nums == "ki" and len(pass_data) < pass_length:
        pass_data += random.choice(integers)

print(f"შემთხვევითი პაროლია: {pass_data}")
# def password_generator():
#     upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
#     integers = "0123456789"
#     pass_data = ""
#     for _ in range(pass_length):
#         if pass_lower == "კი":
#             pass_data += random.choice(lower_alphabet)
#         else:
#             pass
#         if pass_upper == "კი":
#             pass_data += random.choice(upper_alphabet)
#         else:
#             pass
#         if pass_nums == "კი":
#             pass_data += random.choice(integers)
#         else:
#             pass
#     return pass_data
# result = password_generator()
# print(result)