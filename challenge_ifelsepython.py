Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math

import os

import random

import re

import sys







if __name__ == '__main__':

    n = int(input().strip())

check = {True: "Not Weird", False: "Weird"}



print(check[n%2==0

            and (n in range(2,6)

            or n > 20)])