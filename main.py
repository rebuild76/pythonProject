# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def is_leap_year(x):
    return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# str = input("Bla: ")

# try:
#     str = int(str)
# except:
#     print("Fuck Up! Be not so stupid!!!!")
# else:
#     print("Вы ввели {}".format(str))
# finally:
#     print("Exit mother fucker now!")

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(username, password):
    if username in user_database:
        if password == user_database[username]:
            return True
    return False

print(check_user('hesoyam', 'tgm'))