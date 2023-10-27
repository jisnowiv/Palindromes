# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

DEBUG_MODE = False


def debug_print(stuff):
    if DEBUG_MODE:
        print(stuff)


def loop_palindrome(string):
    start_counter = 0
    end_counter = len(string) - 1

    while start_counter < end_counter:
        if string[start_counter] != string[end_counter]:
            return False
        else:
            start_counter += 1
            end_counter -= 1
    return True


def recursive_palindrome(string):
    if type(string) is not str:
        return False

    #   add while loops to strip the non-alpha characters from beginning and end

    if len(string) <= 1:
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    else:
        return recursive_palindrome(string[1:-1])


def dummy_function():
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Recursive Set")
    print(recursive_palindrome("racecar"))                              # true
    print(recursive_palindrome(1234))                                   # false
    print(recursive_palindrome("asdfasdf"))                             # false
    print(recursive_palindrome(dummy_function))                         # false
    print(recursive_palindrome("go hang a salami, i'm a lasagna hog"))  # true

    print("Sort Set")
    print(recursive_palindrome("racecar"))                              # true
    print(recursive_palindrome(1234))                                   # false
    print(recursive_palindrome("asdfasdf"))                             # false
    print(recursive_palindrome(dummy_function))                         # false
    print(recursive_palindrome("go hang a salami, i'm a lasagna hog"))  # true
