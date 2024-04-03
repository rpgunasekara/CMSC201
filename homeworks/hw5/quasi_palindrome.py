"""
File: quasi_palindrome.py
Author: Ravindu Gunasekara
Setion: 44
E-mail: rgunase1@umbc.edu
Date: 10/20/2023
Description:
    User gives a word and a max number of
    errors. Using the function, determines
    if the word qualifies as a
    quasi-palindrome or not.
"""
def quasi_palindrome(word, errors):
    count = 0
# Compares the first half of the word to the latter half.
    for i in range(len(word) // 2):
# Compares i to the final index - i, giving the symmetrical value.
            if word[i] != word[len(word) - 1 - i]:
                count += 1
# Checks if the number of errors in the word are under the allowed amount.
                if count > errors:
                    return False

    return True

if __name__ == "__main__":
    check_word = input("What word do you want to check? ").lower()
    errors_allowed = int(input("How many errors do you want to allow? "))
# "quit" is the only word that can't be checked.
    while check_word != "quit":

        if quasi_palindrome(check_word, errors_allowed) == True:
            print(f"It was a {errors_allowed}-quasi-palindrome!")
        else:
            print(f"It was not a {errors_allowed}-quasi-palindrome!")

        check_word = input("What word do you want to check? ").lower()
        errors_allowed = int(input("How many errors do you want to allow? "))
