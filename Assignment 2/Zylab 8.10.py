#Michelle Oteri
#2252197
def remove_spaces_and_special_chars(input_str):
    return ''.join(char for char in input_str if char.isalnum())


def is_palindrome(input_str):
    input_str = remove_spaces_and_special_chars(input_str.lower())
    return input_str == input_str[::-1]


if __name__ == "__main__":
    user_input = input()
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome")
    else:
        print(f"{user_input} is not a palindrome")