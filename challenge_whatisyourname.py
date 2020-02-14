Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>   def print_full_name(first_name, last_name):

    print("Hello" + " " + first_name + " " + last_name + "! " + "You just delved into python.")



if __name__ == '__main__':

    first_name = input()

    last_name = input()

    print_full_name(first_name, last_name)