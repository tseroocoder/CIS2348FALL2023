Michelle Oteri
2252197

def make_stronger_password(password):
    """Makes a simple password stronger by replacing characters and appending "q*s" to the end.







    Args:



      password: The simple password to make stronger.







    Returns:



      The stronger password.



    """


    replacements = {

        "i": "!",

        "a": "@",

        "m": "M",

        "B": "8",

        "o": "."

    }



    for old_char, new_char in replacements.items():
        password = password.replace(old_char, new_char)



    password += "q*s"

    return password



password = input()

stronger_password = make_stronger_password(password)

print( stronger_password)