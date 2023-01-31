n = "Notable"
lower_case = n.lower()
reverse_word = lower_case[::-1]
if lower_case == reverse_word:
    print("This is a Palindrome")
else:
    print("Not a Palindrome")