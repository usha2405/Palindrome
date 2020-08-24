def palindrome(str):
    string=str.replace(" ","")
    reverse=string[::-1]
    if reverse==string:
        print(f"{str} is a palindrome.")
    else:
        print(f"{str} is not a palindrome")

str=input("Enter a string or number: ")
palindrome(str)
