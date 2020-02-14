Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>   import calendar



m, d, y = map(int, input().split())

print(calendar.day_name[calendar.weekday(y, m, d)].upper())