Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>   def swap_case(s):

    a = ""

    for let in s:

        if let.isupper() == True:

            a+=(let.lower())

        else:

            a+=(let.upper())

    return a

if __name__ == '__main__':

    s = input()

    result = swap_case(s)

    print(result)