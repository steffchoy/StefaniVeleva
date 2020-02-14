Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if __name__ == '__main__':

    a = int(input())

    arr = list(map(int, input().split()))

    b = max(arr)

    i=0

    while(i<a):

        if b ==max(arr):

            arr.remove(max(arr))

        i+=1

print(max(arr))