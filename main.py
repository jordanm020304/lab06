# jordan molina's code?
is_running = True

def encode_and_store(password_str):
    password_list = []
    encoded_password_list = []
    encoded_password_str = ""
    for char in password_str[:]:
        password_list.append(int(char))
    for num in password_list[:]:
        num += 3
        encoded_password_list.append(int(num))

    for num in encoded_password_list[:]:
        encoded_password_str += str(num)

    print('Your password has been encoded and stored!\n')
    print(encoded_password_str)

while is_running:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

    print('Please enter an option: ',end='')
    option_selection = input()

    if option_selection == '1':
        print('Please enter your password to encode: ', end='')
        password_str = input()
        encode_and_store(password_str)

    elif option_selection == '2':

        pass

    elif option_selection == '3':
        is_running = False

















# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
